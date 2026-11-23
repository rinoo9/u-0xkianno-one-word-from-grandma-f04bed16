"""One-word entry for the make.fun bounty 'One Word From Grandma'.

Writes exactly one word to /output/entry.txt: the single word a grandma
would text about AI.

Why "Listening"? A grandma who has just learned that her phone hears
everything does not reach for a technical word -- she names the feeling.
The device is always listening: to her recipes, her gossip, her prayers.
The word is warm (she talks to it like a person), baffled (how does it
know what she was just thinking about?), and suspicious (is someone on
the other end?). One word carries all three at once, which is exactly
how a grandma texts.

Deterministic: no network, no randomness, no environment reads.
"""

import os

WORD = "Listening"


def main() -> None:
    # Gate: the bounty wants exactly one word, 1-30 characters, no
    # surrounding whitespace -- so the entry stays a single word a
    # grandma would actually text, not a sentence or a phrase.
    assert isinstance(WORD, str)
    assert 1 <= len(WORD) <= 30
    assert WORD.strip() == WORD
    assert len(WORD.split()) == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
