# README Badge Generator CLI

A dead simple command-line tool to instantly generate common Markdown badges (Build Status, Code Coverage, PyPI Version, License, Last Commit) for your project's README. No website, no accounts—just a fast CLI that saves you time.

---

## Features

- **Generate 5+ popular badges** for any public GitHub repository.
- **Output**: Ready-to-paste Markdown for your README.
- **Zero config**: No user accounts, no online badge customization, no hassle.
- **Open source, MIT licensed.**

---

## Installation

pip install readme-badge-gen


Or install locally from source for development:

git clone https://github.com/yourusername/readme-badge-gen.git
cd readme-badge-gen
pip install -e


---

## Usage

badge-gen owner/repository


**Options:**
- Specify a PyPI package for the version badge:

    ```
    badge-gen owner/repository --package packagename
    ```

- Only select specific badges (choose from: `build`, `coverage`, `version`, `license`, `last_commit`):

    ```
    badge-gen owner/repository --badges build license
    ```

---

## Example

**Command:**


badge-gen facebook/react


**Output:**
![Build Status](https://img.shields.io/github/actions/workflow/status/facebook](https://img.shields.io/codecov/c/github/facebook/react](https://img.shields.io/p://img.shields.io/github/license](https://img.shields.io/github/last-commit/facebook/react Badges
