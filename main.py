"""SnoozePay: the worst app idea ever pitched.

A dead-serious pitch for an app that lets strangers snooze your alarm
clock for money. Writes the single-sentence pitch to /output/entry.txt.
"""

import os

PITCH = (
    "SnoozePay lets you pay two dollars to snooze a stranger's alarm clock "
    "from anywhere in the world, so your morning is decided by whoever "
    "outbids your will to live."
)


def validate(text: str) -> str:
    """The gate wants UTF-8 text, 1-240 chars, not only whitespace, one
    sentence. Count the pitch, strip stray whitespace, and refuse anything
    that would fail the gate instead of shipping it."""
    text = text.strip()
    if not text:
        raise SystemExit("pitch is empty")
    if len(text) > 240:
        raise SystemExit(f"pitch is {len(text)} chars, must be at most 240")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    return text


def main() -> None:
    text = validate(PITCH)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
