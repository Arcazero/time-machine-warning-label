#!/usr/bin/env python3
"""Funniest Time Machine Warning Label - make.fun entry.

Writes one original one-line warning label for a time machine
(78 characters) to /output/entry.txt, deterministically.
"""

from pathlib import Path

LABEL = "WARNING: If you meet yourself, do not make eye contact. He knows what you did."

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 120


def main() -> None:
    # Self-check against the sealed gate: 1-120 UTF-8 chars, not only whitespace.
    if not LABEL.strip() or len(LABEL) > MAX_CHARS:
        raise SystemExit(f"invalid label: {len(LABEL)} characters (must be 1-{MAX_CHARS})")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LABEL, encoding="utf-8")
    print(f"wrote {len(LABEL)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
