"""One emoji, the one most likely to make a stranger smile, for make.fun."""
import os

OUTPUT_PATH = "/output/entry.txt"

# A hugging face: a smile with open arms. Warm at first glance, readable
# by anyone of any age, and picked rather than the first smiley that comes
# to mind -- with no flirtation or intimacy that would read oddly from a
# stranger. The warmth is in the gesture, not just the grin.
EMOJI = "\U0001f917"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
