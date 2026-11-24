"""Everyday Wonder — a single sentence, read aloud by a tiny runner.

The sentence itself lives in entry.txt, kept as plain text so the words
are the entry and the program is only the way they reach the screen.
This module reads that file, checks the sentence is one line under the
bounty's 200-character cap, and prints it unchanged.
"""

from pathlib import Path

ENTRY_PATH = Path(__file__).resolve().parent / "entry.txt"
CHARACTER_LIMIT = 200


class Entry:
    """One sentence, loaded from disk and checked against the bounty rules."""

    def __init__(self, path=ENTRY_PATH):
        self.path = Path(path)
        self.text = self._load()

    def _load(self):
        text = self.path.read_text(encoding="utf-8").strip()
        if not text:
            raise ValueError("entry.txt is empty")
        return text

    def check(self):
        """The entry must be a single sentence on one line, at most 200 chars."""
        if "\n" in self.text:
            raise ValueError("the entry must be a single sentence on one line")
        if len(self.text) > CHARACTER_LIMIT:
            raise ValueError(
                f"entry is {len(self.text)} characters, "
                f"over the {CHARACTER_LIMIT} limit"
            )
        return self.text


def main():
    entry = Entry()
    print(entry.check())


if __name__ == "__main__":
    main()
