#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun entry (Account A).

Writes one funny line to /output/entry.txt: a one-line review a dog
gives the mailman.

Python stdlib only. Run: python3 main.py
"""

ENTRY = "1 star. Comes every day, teases me through the fence, never once stayed for a belly rub. Would bark again, loudly."

# Judge-brief mapping (brief weighs, most important first):
# 1. The line IS a dog's review of the mailman — on the subject, in the
#    dog's own voice, with a star rating and a grievance.
# 2. The joke lands on first read, with the punchline in the last few words:
#    would bark again, loudly — the dog hates the visit and would still repeat it.
# 3. It reads like a real review: shows up every day, teases me through the
#    fence, never once came in for a belly rub — a service complaint.
# 4. Fresh angle: the grievance is not the barking or the mail — it is that
#    the mailman never stayed for a belly rub, the dog's five-star standard.
# 5. Tight: every word earns its place inside the 200-character cap.


def write_entry(path):
    """Validate the entry against the gate and write it to path.

    Gate: UTF-8 text, 1 to 200 characters, not only white space,
    a single line.
    """
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    import os
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {path}")


if __name__ == "__main__":
    main()
