#!/usr/bin/env python3
"""Funniest Time Machine Warning Label - make.fun entry.

Writes one original one-line warning label for a time machine
(78 characters) to /output/entry.txt, deterministically.
"""

from pathlib import Path

LABEL = "WARNING: If you meet yourself, do not make eye contact. He knows what you did."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LABEL, encoding="utf-8")


if __name__ == "__main__":
    main()
