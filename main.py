#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers: one original fortune-cookie line.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt.
Standard library only, deterministic: the same bytes on every run.
An optional first argument overrides the output path (for local checks);
with no argument the entry is written to /output/entry.txt.
"""

import os
import sys

LINE = "A quiet deploy is the universe's way of saying your tests did their job."


def main() -> None:
    # Gate-guard: the sealed scorer requires UTF-8 text of 1-120
    # characters, not only white space, on a single line. Validate the
    # exact bytes that will be written, before writing them.
    encoded = LINE.encode("utf-8")
    if not 1 <= len(LINE) <= 120:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-120")
    if "\n" in LINE or "\r" in LINE or not LINE.strip():
        raise ValueError("line must be one non-blank line")
    if LINE != LINE.strip():
        raise ValueError("line must not start or end with white space")
    if any(ord(c) < 32 for c in LINE):
        raise ValueError("line must contain no control characters")
    if encoded.decode("utf-8") != LINE:
        raise ValueError("line is not round-trip UTF-8")
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
