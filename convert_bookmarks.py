#!/usr/bin/env python3
"""
Convert Chrome-exported bookmarks HTML file to a formatted plain text file.

This script reads a Chrome bookmarks.html file and converts it to a clean,
well-formatted bookmarks.txt file with folder headers and bookmark entries.
"""

import os
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("beautifulsoup4 is not installed.")
    print("Please install it with: pip install beautifulsoup4")
    sys.exit(1)


def parse_bookmarks(dl_element, folder_name, output_lines):
    """Recursively parse bookmark folders and their contents."""
    output_lines.append("=" * 40 + f" 📁 {folder_name} " + "=" * 40)
    output_lines.append("")

    container = dl_element
    p_tag = dl_element.find("p")
    if p_tag:
        container = p_tag

    dt_elements = container.find_all("dt", recursive=False)

    for dt in dt_elements:
        h3 = dt.find("h3", recursive=False)
        if h3:
            sub_folder_name = h3.get_text().strip()
            nested_dl = dt.find("dl")
            if nested_dl:
                output_lines.append("")
                parse_bookmarks(nested_dl, sub_folder_name, output_lines)
        else:
            a = dt.find("a", recursive=False)
            if a:
                title = a.get_text().strip()
                href = a.get("href", "").strip()
                if href:
                    output_lines.append(f"  • {title}")
                    output_lines.append(f"    🔗 {href}")
                    output_lines.append("")


def find_bookmarks_bar_dl(soup):
    """Find the DL element containing the Bookmarks bar or other root folder."""
    root_dl = soup.find("dl")
    if not root_dl:
        return None, "BOOKMARKS BAR"

    p = root_dl.find("p", recursive=False)
    if p:
        first_dt = p.find("dt", recursive=False)
    else:
        first_dt = root_dl.find("dt", recursive=False)

    if first_dt:
        h3 = first_dt.find("h3", recursive=False)
        if h3:
            nested_dl = first_dt.find("dl")
            if nested_dl:
                return nested_dl, h3.get_text().strip()

    return root_dl, "BOOKMARKS BAR"


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(script_dir, "bookmarks.html")
    txt_path = os.path.join(script_dir, "bookmarks.txt")

    if not os.path.exists(html_path):
        print("bookmarks.html not found in the script directory")
        sys.exit(1)

    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading bookmarks.html: {e}")
        sys.exit(1)

    soup = BeautifulSoup(html_content, "html.parser")
    root_dl, root_folder_name = find_bookmarks_bar_dl(soup)

    if root_dl is None:
        print("No bookmark structure found in the HTML file")
        sys.exit(1)

    output_lines = []
    parse_bookmarks(root_dl, root_folder_name, output_lines)

    while output_lines and output_lines[-1] == "":
        output_lines.pop()

    try:
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))
    except Exception as e:
        print(f"Error writing bookmarks.txt: {e}")
        sys.exit(1)

    print("Done! bookmarks.txt has been created successfully.")


if __name__ == "__main__":
    main()
