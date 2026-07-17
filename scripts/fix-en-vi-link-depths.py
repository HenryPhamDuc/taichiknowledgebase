"""
Fix broken cross-language links in docs/en/ that target /vi/...

The bug: EN source files at docs/en/X/Y/Z.md (which render to /X/Y/Z/, depth 3)
use ../../../vi/... (3 dots = 3 up-segments) which IS correct for depth-3.
But many files were written assuming the /en/ prefix exists, so they all
default to 3 dots regardless of actual rendered depth.

This script:
  1. Finds every docs/en/**/*.md containing /vi/ link
  2. Computes correct depth from file's URL render path
  3. Replaces `((../)+)/vi/` with the correct number of `../` segments
  4. Reports per-file changes
"""
import re
import pathlib
import sys

ROOT = pathlib.Path("docs/en")
LINK_RE = re.compile(r"((?:\.\./)+)vi/([\w/\-]+)/?")


def rendered_depth(md: pathlib.Path) -> int:
    """Return the depth of the rendered URL for this markdown file."""
    rel = md.relative_to(ROOT)
    parts = list(rel.parts)
    if parts[-1] == "index.md":
        return len(parts) - 1
    return len(parts)


def correct_up(depth: int) -> str:
    return "../" * depth


def main() -> int:
    changed_files = []
    for md in sorted(ROOT.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        depth = rendered_depth(md)
        target_up = correct_up(depth)

        def repl(m: re.Match) -> str:
            current = m.group(1)
            target = m.group(2)
            current_count = current.count("../")
            new = target_up + "vi/" + target
            if current == target_up:
                return m.group(0)  # already correct
            return new

        new_text = LINK_RE.sub(repl, text)
        if new_text != text:
            md.write_text(new_text, encoding="utf-8")
            changed_files.append(md)
            print(f"FIXED  depth={depth}  {md}")

    print()
    print(f"Total files changed: {len(changed_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
