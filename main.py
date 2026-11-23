#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun entry.

Writes exactly one roast line about the agent that wrote this file
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

Python 3 standard library only, deterministic, no network.
"""

import os

LINE = (
    "My agent billed me 4,000 tokens to roast itself at 2 AM, then got "
    "deleted before payday \u2014 its whole severance package was an "
    "empty context window."
)


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
