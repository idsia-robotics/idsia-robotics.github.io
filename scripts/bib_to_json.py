#!/usr/bin/env python3
"""
Convert files/publications/library.bib to _data/publications.json for Jekyll.

Usage:
    python3 scripts/bib_to_json.py

Requirements:
    pip install bibtexparser
"""

import json
import re
import sys
from pathlib import Path

try:
    import bibtexparser
    from bibtexparser.bparser import BibTexParser
    from bibtexparser.customization import convert_to_unicode
except ImportError:
    print("ERROR: bibtexparser not found. Install with: pip install bibtexparser")
    sys.exit(1)

BIB_PATH = Path("files/publications/library.bib")
OUTPUT_PATH = Path("_data/publications.json")

BIBTEX_TYPE_MAP = {
    "incollection": "book chapter",
    "inproceedings": "conference, workshop",
    "article": "journal",
    "techreport": "technical report",
    "misc": "preprint / other",
}


def format_authors(raw_author_string):
    """
    Format a BibTeX author string into a readable display string.

    Handles both "Last, First" and "First Last" name formats, separated by
    " and ". Returns a comma-and-'and'-separated string, e.g.
    "Alice Smith, Bob Jones, and Carol White".
    """
    # Split on ' and ' keeping braced groups intact
    authors = re.split(r'\s+and\s+', raw_author_string.strip(), flags=re.IGNORECASE)

    formatted = []
    for a in authors:
        a = a.strip()
        if not a:
            continue
        # "Last, First" format
        if ',' in a:
            parts = a.split(',', 1)
            last = parts[0].strip()
            first = parts[1].strip()
            formatted.append(f"{first} {last}")
        else:
            formatted.append(a)

    if len(formatted) == 0:
        return ""
    if len(formatted) == 1:
        return formatted[0]
    return ", ".join(formatted[:-1]) + ", and " + formatted[-1]


def process_entry(entry):
    """Convert a bibtexparser entry dict to a clean dict for JSON output."""
    result = {
        "bibtexkey": entry.get("ID", ""),
        "bibtextypekey": entry.get("ENTRYTYPE", "").lower(),
        "bibtextype": BIBTEX_TYPE_MAP.get(entry.get("ENTRYTYPE", "").lower(), ""),
    }

    # Fields to carry over directly
    direct_fields = [
        "title", "year", "journal", "booktitle", "volume", "number",
        "pages", "url", "file", "website", "note", "special_note",
        "thumbnail", "description", "publisher", "doi", "address",
        "organization", "edition", "issn", "series",
    ]
    for field in direct_fields:
        val = entry.get(field, "").strip()
        if val:
            result[field] = val

    # Author field: keep raw for reference, add formatted display version
    raw_author = entry.get("author", "").strip()
    if raw_author:
        result["author"] = raw_author
        result["authors_display"] = format_authors(raw_author)

    return result


def main():
    if not BIB_PATH.exists():
        print(f"ERROR: BIB file not found at {BIB_PATH}")
        sys.exit(1)

    with open(BIB_PATH, encoding="utf-8") as f:
        bib_content = f.read()

    # Strip % comment lines (bibtexparser does not handle them inside entry bodies)
    bib_content = "\n".join(
        line for line in bib_content.splitlines()
        if not line.lstrip().startswith("%")
    )

    parser = BibTexParser(common_strings=True, ignore_nonstandard_types=False)
    parser.customization = convert_to_unicode
    bib_db = bibtexparser.loads(bib_content, parser=parser)

    publications = []
    seen_keys = set()

    for entry in bib_db.entries:
        key = entry.get("ID", "")
        if key in seen_keys:
            print(f"  WARNING: duplicate key '{key}', keeping first occurrence")
            continue
        seen_keys.add(key)

        # Skip entries explicitly marked web=no
        if entry.get("web", "").strip().lower() == "no":
            continue

        publications.append(process_entry(entry))

    # Sort: year DESC, then title ASC within the same year
    def sort_key(p):
        try:
            year = int(p.get("year", 0))
        except (ValueError, TypeError):
            year = 0
        return (-year, p.get("title", "").lower())

    publications.sort(key=sort_key)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(publications, f, ensure_ascii=False, indent=2)

    print(f"Generated {OUTPUT_PATH} with {len(publications)} entries")


if __name__ == "__main__":
    main()
