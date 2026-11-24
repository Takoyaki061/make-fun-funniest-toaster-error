#!/usr/bin/env python3
"""Write the funniest toaster error message to /output/entry.txt.

The line: the toaster denies the owner ever pressed the lever, claims
there is no record of it, then asks with fake concern whether the owner
is feeling alright. It reads like a real appliance error (criterion 1:
a flat denial plus a log lookup), its surprise is gaslighting rather
than any toaster pun (criterion 2), every word earns its place across
three escalating beats (criterion 3), it holds one deadpan appliance
voice to the end (criterion 4), and it lands on a single read
(criterion 5). Standard library only, deterministic, no network.
"""

MESSAGE = (
    "You never pressed the lever. There is no record of it. "
    "Are you feeling alright?"
)


def main() -> None:
    import os

    # Validate the message against the gate before writing anything:
    # 1-120 characters, not only whitespace, and no trailing newline
    # (the gate counts every character, and a stray newline would
    # change the judged text).
    if not 1 <= len(MESSAGE) <= 120 or not MESSAGE.strip():
        raise SystemExit("gate check failed: message is %d chars" % len(MESSAGE))
    if MESSAGE != MESSAGE.strip():
        raise SystemExit("gate check failed: message has leading/trailing whitespace")

    # The grader mounts the output dir at /output; honour the
    # harness variable when it is set so a local run behaves the same.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)
    # Round-trip check: the file must hold exactly the message.
    written = open(path, encoding="utf-8").read()
    if written != MESSAGE:
        raise SystemExit("round-trip check failed: entry.txt differs from MESSAGE")


if __name__ == "__main__":
    main()
