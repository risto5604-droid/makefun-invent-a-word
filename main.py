#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-deranalabs-invent-a-word-we-need-17a020e0 ("Invent a Word We Need").

The entry coins one new word: "promptigue" — the exhaustion of
rewording the same request to an AI for the fifth time, hoping this
phrasing finally works. One concrete scene (the fifth rewording),
one specific twist (the hope that this phrasing is finally the one).
"""
import os

LINE = "promptigue (n.): the exhaustion of rewording the same request to an AI for the fifth time, hoping this phrasing finally works."

# Gate: exactly one line, 1-140 characters, ASCII only, not blank.
# The tight gate is what the entry is graded on: word + definition
# together at most 140 characters, in a single line.
assert 1 <= len(LINE) <= 140 and LINE.isascii() and LINE.strip() and "\n" not in LINE, "entry line violates the one-line 1-140 character ASCII gate"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
