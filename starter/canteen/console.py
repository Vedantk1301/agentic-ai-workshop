"""Small helpers so the demos print cleanly on a Windows projector."""

from __future__ import annotations

import os
import sys


def setup(scenario: str | None = None) -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    if scenario:
        os.environ["SCENARIO"] = scenario


def banner(title: str) -> None:
    line = "=" * len(title)
    print(f"\n{line}\n{title}\n{line}")


def pause(enabled: bool, prompt: str = "   (press Enter to reveal the next step) ") -> None:
    if enabled:
        input(prompt)
