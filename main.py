#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun entry.

Writes one short text to /output/entry.txt: a cat that hears the thunder,
registers it, and stays exactly where it is. One concrete image, shown
rather than instructed. Pure standard library, no network, deterministic:
every run writes the same bytes.

Usage: python3 main.py [output_path]   (default /output/entry.txt)
"""

import os
import sys

# The entry text: 224 Unicode code points, inside the 1-280 gate.
TEXT = (
    "A cat sleeps through thunder. Not because it cannot hear \u2014 its ear "
    "turns at every rumble \u2014 but because it has decided the sound is not "
    "its business. It breathes out, longer than it breathes in, and stays "
    "exactly where it is."
)


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
