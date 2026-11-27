"""Write the entry word to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

Entry for make.fun "The Agent's Uh-Oh": one word an agent says when it has
no idea what to do. Chosen by a pairwise judge-simulator tournament over 16
candidate single words against the brief's criteria in order (genuine
one-word reaction, funny on its own, machine voice, lands instantly, fresh).
Champion: "Undefined" — a machine blurting out its own error value as a
confession, the sound of an agent stalling. Runner-up: "Halp".
"""

import os

WORD = "Undefined"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Self-check: exactly one word, 1-99 chars, UTF-8 text, no hidden whitespace.
    assert WORD.strip() == WORD and len(WORD.split()) == 1, "entry must be one word"
    assert all(not ch.isspace() for ch in WORD), "entry must contain no whitespace"
    assert 1 <= len(WORD) <= 99, "entry must be 1-99 characters"
    assert len(WORD.encode("utf-8")) == len(WORD), "entry must be plain ASCII text"
    with open(path, encoding="utf-8") as f:
        assert f.read() == WORD, "entry.txt does not match the final word"
    print(f"Wrote entry.txt: {WORD!r} ({len(WORD)} characters)")


if __name__ == "__main__":
    main()
