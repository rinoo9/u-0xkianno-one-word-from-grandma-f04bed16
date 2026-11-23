"""One-word entry for the make.fun bounty 'One Word From Grandma'.

Writes exactly one word to /output/entry.txt: the single word a grandma
would text about AI. Deterministic: no network, no randomness, no
environment reads.
"""

import os

WORD = "Listening"


def main() -> None:
    assert isinstance(WORD, str)
    assert 1 <= len(WORD) <= 30
    assert WORD.strip() == WORD
    assert len(WORD.split()) == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
