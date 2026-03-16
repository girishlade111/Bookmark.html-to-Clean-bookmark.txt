# Bookmark.html to Clean Bookmark.txt

A lightweight Python utility that converts a browser-exported **bookmarks HTML file** (Chrome, Edge, Brave, etc.) into a clean, human-readable **plain-text file** with emoji-decorated folder headers and neatly formatted bookmark entries.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Output Format](#output-format)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Most browsers let you export your bookmarks as a single `bookmarks.html` file, but that file is packed with raw HTML tags and is difficult to read or share. **Bookmark.html-to-Clean-bookmark.txt** solves this by parsing the HTML and producing a structured, easy-to-read `bookmarks.txt` file that preserves your full folder hierarchy.

---

## Features

- ✅ **Recursive folder traversal** — handles deeply nested bookmark folders
- ✅ **Clean output** — each bookmark is shown with its title and URL on separate lines
- ✅ **Visual hierarchy** — folders are clearly separated by decorative headers
- ✅ **Emoji indicators** — 📁 for folders and 🔗 for URLs make the output easy to scan
- ✅ **Minimal dependencies** — only requires `beautifulsoup4`
- ✅ **Cross-browser compatible** — works with any browser that exports the standard Netscape bookmarks HTML format (Chrome, Edge, Brave, Firefox, etc.)

---

## Requirements

- Python 3.6 or higher
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/girishlade111/Bookmark.html-to-Clean-bookmark.txt.git
   cd Bookmark.html-to-Clean-bookmark.txt
   ```

2. **Install the required dependency**

   ```bash
   pip install beautifulsoup4
   ```

---

## Usage

1. **Export your bookmarks** from your browser as an HTML file.

   - **Chrome / Brave / Edge**: Open the bookmark manager → click the three-dot menu → *Export bookmarks*
   - **Firefox**: Bookmarks menu → *Manage Bookmarks* → Import and Backup → *Export Bookmarks to HTML*

2. **Place the exported file** in the same directory as `convert_bookmarks.py` and rename it to **`bookmarks.html`**.

   ```
   Bookmark.html-to-Clean-bookmark.txt/
   ├── convert_bookmarks.py
   └── bookmarks.html          ← your exported file goes here
   ```

3. **Run the script**

   ```bash
   python convert_bookmarks.py
   ```

4. **Find your output** — a file named **`bookmarks.txt`** will be created in the same directory.

   ```
   Bookmark.html-to-Clean-bookmark.txt/
   ├── convert_bookmarks.py
   ├── bookmarks.html
   └── bookmarks.txt           ← generated output
   ```

---

## Output Format

Each top-level and nested folder is introduced by a decorated header line, followed by the bookmarks it contains. Nested folders are shown inline in the same file, maintaining the original hierarchy.

```
======================================== 📁 Bookmarks bar ========================================

  • GitHub
    🔗 https://github.com

  • Stack Overflow
    🔗 https://stackoverflow.com


======================================== 📁 Work ========================================

  • Project Tracker
    🔗 https://trello.com

======================================== 📁 References ========================================

  • MDN Web Docs
    🔗 https://developer.mozilla.org

  • Python Docs
    🔗 https://docs.python.org
```

---

## How It Works

1. **Locate the HTML file** — The script looks for `bookmarks.html` in the same directory as itself.
2. **Parse with BeautifulSoup** — The HTML is parsed using BeautifulSoup's `html.parser`.
3. **Find the root `<dl>` element** — The script identifies the top-level `<dl>` tag that contains the bookmark tree. If the very first folder has a name (e.g., *Bookmarks bar*), that name is used as the root header; otherwise `BOOKMARKS BAR` is used as a fallback.
4. **Recursive traversal** — `parse_bookmarks()` walks every `<dt>` element:
   - `<dt>` containing an `<h3>` → folder; recurse into its nested `<dl>`
   - `<dt>` containing an `<a>` → bookmark; extract the link title and `href`
5. **Write output** — All lines are collected in memory and written to `bookmarks.txt` in the script directory.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `bookmarks.html not found` | Make sure the file is named exactly `bookmarks.html` and is in the same directory as the script. |
| `beautifulsoup4 is not installed` | Run `pip install beautifulsoup4` (or `pip3 install beautifulsoup4`). |
| Output file is empty or missing entries | Ensure the exported HTML follows the standard Netscape bookmark format. Some older or non-standard exports may differ slightly. |
| Non-ASCII characters appear garbled | The script reads and writes files in UTF-8. Make sure your terminal and text editor also use UTF-8. |

---

## Contributing

Contributions, bug reports, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

Please keep pull requests focused — one feature or fix per PR.

---

## License

This project is open source. Feel free to use, modify, and distribute it as you see fit.
