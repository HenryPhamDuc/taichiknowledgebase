#!/usr/bin/env python
"""
Post-build: mirror the site root (default language = EN) to site/en/ so
that /en/ serves the same content as /. Workaround for mkdocs-static-i18n
v1.3.1 not exposing a config option to also build the default language at
its own prefix.
"""
import os
import shutil
import sys
from pathlib import Path

def main() -> int:
    site = Path("site")
    if not site.is_dir():
        print("ERROR: site/ does not exist. Run `mkdocs build` first.", file=sys.stderr)
        return 1

    mirror = site / "en"
    if mirror.exists():
        shutil.rmtree(mirror)
    mirror.mkdir()

    # Copy each top-level entry except "en" itself (no recursion into mirror)
    count = 0
    for entry in site.iterdir():
        if entry.name == "en":
            continue
        dest = mirror / entry.name
        if entry.is_dir():
            shutil.copytree(entry, dest)
        else:
            shutil.copy2(entry, dest)
        count += 1
    print(f"Mirrored {count} top-level entries to {mirror}/")
    return 0

if __name__ == "__main__":
    sys.exit(main())
