"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum's deadpan excuse for missing one spot, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Stdlib only.
"""

import os
import sys

ENTRY = (
    "I detected the spot, mapped it, circled it twice, then left it alone: "
    "it was the cat's favourite napping patch, and my warranty does not "
    "cover starting wars."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or "\n" in text or len(text) > 200:
        print("entry must be a single line of 1-200 characters", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Best-effort copy next to this script, for local inspection.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w",
                  encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
