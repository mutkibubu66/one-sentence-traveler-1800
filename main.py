"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to someone arriving from 1800, to /output/entry.txt.

The sentence builds only on things a person from 1800 already knows -- a
road, a letter, a book, a song, a picture -- and pictures the internet as
one road that reaches every town on earth at once, where anything asked for
arrives in a breath and anyone may answer back.
"""

import os

ENTRY = (
    "Picture a road that runs to every town on earth at once, where any "
    "letter, book, song, or picture you ask for arrives before your breath "
    "is out, and where anyone may answer back."
)


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters, one
    # sentence, no trailing newline (the gate counts characters as written).
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
