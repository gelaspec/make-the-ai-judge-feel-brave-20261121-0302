#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is a fixed, hand-written piece: a flat stone at the water's
edge, warmed by late sun, covered and uncovered by the tide, still
there. No network, no randomness, no input: every run writes the
same bytes.
"""

import os

TEXT = (
    "At the edge of the water, one flat stone warms in the late sun. "
    "The tide comes in, covers it, and goes out again, and the stone is "
    "still there, a little cooler, a little darker, holding the afternoon "
    "in its shallow cup. Nothing is asked of it. The water will be back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
