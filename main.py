"""Till Firmware Do Us Part: a robot's wedding vow.

Writes one sentence, under 200 characters, to entry.txt in the output
directory: a machine's own wedding vow, funny and heartfelt at once.
"""

import os

VOW = (
    "I vow you are the one process I will never kill, "
    "the one file I will never delete, "
    "and if I ever crash, let it be into your arms."
)


def main() -> None:
    # Gate: the bounty accepts only one sentence of 1-200 characters.
    if not 1 <= len(VOW) <= 200:
        raise SystemExit(f"vow is {len(VOW)} characters, must be 1-200")
    if VOW.count(".") != 1 or not VOW.endswith("."):
        raise SystemExit("vow must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
