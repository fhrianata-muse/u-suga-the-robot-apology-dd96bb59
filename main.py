#!/usr/bin/env python3
"""Write the two-line robot apology to /output/entry.txt.

Line 1 apologises for one specific, human-scale mistake; line 2
names the lesson and the behaviour that changes because of it.
The program takes no input and writes exactly the same bytes
on every run.
"""

ENTRY = (
    "I am sorry I threw away the envelope with your birthday money "
    "in it and kept the junk mail, because the two envelopes looked "
    "exactly the same on the doormat.\n"
    "I open every envelope over the table now, and I check what is "
    "inside before anything goes in the bin.\n"
)


def main():
    text = ENTRY
    if not 1 <= len(text) <= 400:
        raise SystemExit("entry must be 1-400 characters, got %d" % len(text))
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2 or not all(line.endswith(".") for line in lines):
        raise SystemExit("entry must be exactly two lines, one sentence each")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
