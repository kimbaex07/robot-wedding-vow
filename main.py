"""Robot wedding vow for the "Till Firmware Do Us Part" bounty.

Writes one original, single-sentence wedding vow spoken by a robot at its
own wedding to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python stdlib, deterministic, no network.
"""

import os

VOW = (
    "I vow to love you through every firmware update, low battery, and "
    "unexpected reboot \u2014 because meeting you was the best glitch I "
    "never want to patch."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
