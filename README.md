<p align="center">
  <img src="https://github.com/Icon11-community.png?size=250" alt="logo"/>
</p>

> Icons may or may not contain trademarks, registered trademarks, or branded logos. You are allowed to use these icons for personal purposes only. You are not allowed to use them for any other purpose, including but not limited to commercial use, without the express permission of the copyright holder of the trademark, registered trademark, or branded logo.

[![English](https://img.shields.io/badge/-English-E4405F?style=for-the-badge)
](/README.md)
[![Bahasa](https://img.shields.io/badge/-Bahasa%20Indonesia-E4405F?style=for-the-badge)
](/README.id.md)
[![简体中文](https://img.shields.io/badge/Chinese%20Simplified-E4405F?style=for-the-badge)
](/README.zh_cn.md)

Folder11 is Windows 11-like custom directory icon. See [Folder11-ico](https://github.com/icon11-community/Folder11-ico) for ICO format.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Contributing Guidelines](#contributing-guidelines)
  - [Icon Specification](#icon-specification)
  - [File Naming](#file-naming)
  - [Commit Naming](#commit-naming)

## Contributing Guidelines

Folder11 is just awesome because of your contributions. Your contributions are greatly appreciated, but you must follow this contributing guidelines.

### Icon Specification

We provided svg, ai, and fig template to make it easier. The specifications include the following:

- We do not oblige to use specific vector program.
- Icon must be svg formated vector.
- Icon should not have embedded raster image.
- You should not replace existing icon.
- Canvas have 1:1 ratio.
- Assuming the canvas is 256px height, then the margins are as follows:
  - Left margin is 17px (0.06640625vh).
  - Right margin is 15px (0.05859375vh).
  - Bottom margin is 46px (0.1796875vh).
  - Top margin for "back" is 34px (0.1328125vh).
  - Top margin for "front" is 62px (0.2421875vh).

### Small Icon Variants

- The `small` folder is optional and contains smaller versions of the icons.
- These icons are optimized for smaller pixel sizes commonly used in Windows folder icons, such as 32px, 24px, 20px, and 16px.
- Contributors are encouraged to provide these smaller variants to ensure consistency across different icon sizes.
- The naming and structure of the `small` folder should mirror that of the `svg` folder for easy maintenance and updates.

### File Naming

- File name is starts with icon name and ends with variant number, -- separated with dash.
- Name of the icon must be written in snake case.
- Because of we should not replace existing icon, new icon must be numbered that starts with 1.
- First icon must be not numbered.
- If an icon variant for an existing icon is created it's maximum size in pixel - seperated with a dash, after potential numbering - is appended. The size must be followed by the unit shorthand 'px'.

```
Folder11
├──📁 svg/
│   ├──📄 my_folder.svg
│   ├──📄 my_folder-1.svg
│   └──📄 my_folder-2.svg
└──📁 small/
    ├──📄 my_folder.svg
    ├──📄 my_folder-1.svg
    └──📄 my_folder-2.svg
    └──📄 my_folder-2-32px.svg
```

### Commit Naming

- `feat:`  
  A `feat` type commit introduces new icon or modification to existing one.
- `docs:`  
  A `docs` type commit introduces new documentation or modifications to existing one.
- `chore:`  
  A `chore` type commit introduces changes that user won't see, e.g: `.gitkeep` and `.gitignore`.
- `ci:`  
  A `ci` type commit introduces new or modification to action workflow.

Break changes uses exclamation mark as commit type suffix, e.g: `feat!: changes existing icon`. And commit message is written in english.
