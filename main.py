"""One Line, One Laugh -- make.fun entry.

Writes a single original one-liner to /output/entry.txt. The line is a
constant, so every run produces byte-identical output. At 92 characters
it sits well inside the gate of 1 to 200 characters.
"""

import os

LINE = "I told the printer it was out of ink, so it printed its resignation letter in perfect color."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
