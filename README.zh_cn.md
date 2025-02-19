<p align="center">
  <img src="https://github.com/Icon11-community.png?size=250" alt="logo"/>
</p>

> 图标可能包含或不包含商标、注册商标或品牌标志。您仅可出于个人目的使用这些图标。未经商标、注册商标或品牌标志的版权所有者明确许可，您不得将它们用于任何其他目的，包括但不限于商业用途。

[![English](https://img.shields.io/badge/-English-E4405F?style=for-the-badge)
](/README.md)
[![Bahasa](https://img.shields.io/badge/-Bahasa%20Indonesia-E4405F?style=for-the-badge)
](/README.id.md)
[![Chinese - Simplified](https://img.shields.io/badge/Chinese%20Simplified-E4405F?style=for-the-badge)
](/README.zh_cn.md)

Folder11 是类似 Windows 11 的文件夹图标。可以到[Folder11-ico](https://github.com/icon11-community/Folder11-ico)获取 ICO 格式。

## 目录

- [目录](#table-of-contents)
- [贡献指南](#contributing-guidelines)
  - [图标规范](#icon-specification)
  - [文件命名](#file-naming)
  - [提交规范](#commit-naming)

## 贡献指南

Folder11 之所以如此出色，正是因为社区的贡献。十分感谢您的贡献，但您必须遵循以下贡献指南。

### 图标规范

我们提供了 svg、ai 和 fig 模板，使其更易于使用。规格包括以下内容：

- 我们不强制使用特定的矢量程序。
- 图标必须是 svg 格式的矢量图。
- 图标不应嵌入位图图像。
- 您不应替换现有图标。
- Canvas 具有 1:1 的比例。
- 假设画布高度为 256 像素，则边距如下：
  - 左边距为 17 像素（0.06640625vh）。
  - 右边距为 15 像素（0.05859375vh）。
  - 底部边距为 46 像素（0.1796875vh）。
  - 后面的顶部边距为 34px（0.1328125vh）。
  - 前面的顶部边距为 62 像素（0.2421875vh）。

### 文件命名

- 文件名以图标名称开头，以变体编号结尾，由破折号分隔。
- 图标名称必须使用蛇形命名法编写。
- 由于我们不应替换现有图标，新图标必须编号，从 1 开始。
- 第一个图标不应编号。

```
Folder11
└──📁 svg/
    ├──📄 my_folder.svg
    ├──📄 my_folder-1.svg
    └──📄 my_folder-2.svg
```

### 提交命名

- `feat:`
  - `feat` 类型提交引入了新的图标或对现有图标的修改。
- `docs:`
  - `docs` 类型提交引入了新的文档或对现有文档的修改。
- `chore:`
  - `chore` 类型提交引入了用户看不到的更改，例如：`.gitkeep` 和 `.gitignore`。
- `ci:`
  - `ci` 类型提交引入了新的或修改了动作工作流程。

变更使用感叹号作为提交类型后缀，例如：`feat!: 更改现有图标`。提交信息请使用英文编写。
