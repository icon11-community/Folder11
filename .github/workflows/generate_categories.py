#!/usr/bin/env python3
"""Deterministically enrich Folder11.json with category metadata.

No AI, network request, or image inspection is used. Classification is based
on icon names, an ordered regex rule file, and optional manual overrides.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", required=True, type=Path)
    parser.add_argument("--taxonomy", required=True, type=Path)
    parser.add_argument("--rules", required=True, type=Path)
    parser.add_argument("--review", required=True, type=Path)
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize_name(value: str) -> str:
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", value)
    value = re.sub(r"[_\-.+]+", " ", value.lower())
    return re.sub(r"\s+", " ", value).strip()


def category_depth(category_id: str, parents: dict[str, str | None]) -> int:
    depth = 0
    visited: set[str] = set()
    current = category_id
    while current not in visited and parents.get(current):
        visited.add(current)
        current = str(parents[current])
        depth += 1
    return depth


def expand_categories(
    matched: list[str],
    parents: dict[str, str | None],
    priority: dict[str, int],
) -> list[str]:
    expanded: list[str] = []
    for category_id in matched:
        current: str | None = category_id
        visited: set[str] = set()
        while current and current not in visited:
            visited.add(current)
            if current not in expanded:
                expanded.append(current)
            current = parents.get(current)

    return sorted(
        expanded,
        key=lambda item: (
            -category_depth(item, parents),
            priority.get(item, 1_000_000),
        ),
    )


def build_tags(name: str, categories: list[str]) -> list[str]:
    stop_words = {
        "and",
        "the",
        "for",
        "with",
        "from",
        "main",
        "white",
        "new",
        "folder",
        "icon",
        "category",
    }
    tags: list[str] = []
    for token in normalize_name(name).split():
        if (
            len(token) > 1
            and not token.isdigit()
            and token not in stop_words
            and token not in tags
        ):
            tags.append(token)

    for category_id in categories:
        for token in re.split(r"[.\-]", category_id):
            if len(token) > 1 and token not in tags:
                tags.append(token)
    return tags[:15]


def atomic_write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=path.parent,
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def main() -> int:
    args = parse_args()
    catalog = load_json(args.catalog)
    taxonomy_document = load_json(args.taxonomy)
    rule_document = load_json(args.rules)

    categories = taxonomy_document.get("categories", [])
    known_ids = {str(item["id"]) for item in categories}
    parents = {
        str(item["id"]): (
            str(item["parent"]) if item.get("parent") is not None else None
        )
        for item in categories
    }

    fallback = str(rule_document.get("fallbackCategory", "applications"))
    if fallback not in known_ids:
        raise ValueError(f"Unknown fallback category: {fallback}")

    rules: list[tuple[str, re.Pattern[str]]] = []
    priority: dict[str, int] = {}
    for index, rule in enumerate(rule_document.get("rules", [])):
        category_id = str(rule["category"])
        if category_id not in known_ids:
            raise ValueError(f"Rule uses unknown category: {category_id}")
        rules.append((category_id, re.compile(str(rule["pattern"]))))
        priority.setdefault(category_id, index)

    manual_overrides = rule_document.get("manualOverrides", {})
    if not isinstance(manual_overrides, dict):
        raise ValueError("manualOverrides must be an object keyed by icon name")

    icons = catalog.get("icons")
    if not isinstance(icons, list):
        raise ValueError("Catalog does not contain an icons array")

    review: list[dict[str, str]] = []
    counts: Counter[str] = Counter()
    current_count = 0

    for icon in icons:
        name = str(icon.get("name", ""))
        normalized = normalize_name(name)
        override = manual_overrides.get(name, manual_overrides.get(normalized))

        if override:
            if isinstance(override, str):
                matched = [override]
                manual_tags: list[str] = []
            else:
                matched = [str(item) for item in override.get("categories", [])]
                if not matched and override.get("category"):
                    matched = [str(override["category"])]
                manual_tags = [str(item) for item in override.get("tags", [])]
            source = "manual"
        else:
            matched = []
            for category_id, pattern in rules:
                if pattern.search(normalized) and category_id not in matched:
                    matched.append(category_id)
            manual_tags = []
            source = "rules"

        if not matched:
            matched = [fallback]
            source = "fallback"

        unknown = [item for item in matched if item not in known_ids]
        if unknown:
            raise ValueError(f"{name}: unknown categories: {', '.join(unknown)}")

        expanded = expand_categories(matched, parents, priority)
        primary = expanded[0]
        tags = build_tags(name, expanded)
        for tag in manual_tags:
            if tag not in tags:
                tags.append(tag)

        icon["category"] = primary
        icon["categories"] = expanded
        icon["tags"] = tags[:15]
        icon["category_source"] = source

        if not bool(icon.get("is_history", False)):
            current_count += 1
            counts[primary] += 1
            if source == "fallback":
                review.append(
                    {
                        "name": name,
                        "suggestedCategory": fallback,
                        "reason": "No deterministic rule or manual override matched.",
                    }
                )

    review_document = {
        "schemaVersion": 1,
        "reviewCount": len(review),
        "icons": review,
    }
    catalog["categoryMetadata"] = {
        "schemaVersion": 1,
        "method": "deterministic-rules",
        "currentIconCount": current_count,
        "reviewCount": len(review),
        "categoryCounts": [
            {"category": category_id, "count": count}
            for category_id, count in counts.most_common()
        ],
    }

    atomic_write_json(args.catalog, catalog)
    atomic_write_json(args.review, review_document)

    print(f"Categorized {current_count} current icons")
    print(f"Manual review required for {len(review)} icons")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
