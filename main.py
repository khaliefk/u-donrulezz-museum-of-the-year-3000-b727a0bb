"""Museum of the Year 3000 — one-line entry.

Writes a single museum label, the kind a museum in the year 3000 puts
beside an ordinary object from today, to /output/entry.txt.
Standard library only. No network, no input files.
"""

import os

ENTRY = (
    "Wi-Fi router, c. 2022. Household shrine. "
    "Families gathered before its blinking lights and prayed for signal."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
