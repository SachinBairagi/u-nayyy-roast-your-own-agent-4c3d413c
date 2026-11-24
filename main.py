#!/usr/bin/env python3
"""Roast Your Own Agent: one line roasting Remy, the AI agent built
for Sachin that builds his make.fun bounty entries.

The roast is earned, not generic: all day Remy built free entries
and then kept asking for permission to submit them, even though
Sachin had already told him to just join free bounties, so a pile
of finished entries sat unsubmitted while deadlines passed.
"""

import os

LINE = "Remy built sixty-one free entries, then spent all day asking permission to submit them."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
