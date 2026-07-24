"""
Progress/resume helper for LEARN_PYTHON. Run via `./start.sh` from the
project root, not directly — start.sh handles activating the venv first.

What this does:
1. Reads the syllabus straight out of README.md's "## Progress" checklist,
   so there's exactly one place the module list is maintained.
2. For each module that actually exists on disk, runs its test suite
   (quietly) to see if it's fully passing.
3. Prints a progress bar and tells you exactly which module to resume,
   with the exact commands to run.

This is infrastructure, not a curriculum exercise — you're not expected to
read or extend this file as part of the course, though nothing here is
off limits if you're curious later (Module 09, Files & the Filesystem, and
Module 12, Modules & Packages, cover most of what this script uses).
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

try:
    from rich.console import Console
    from rich.panel import Panel

    console = Console()
except ImportError:
    console = None


ROOT = Path(__file__).resolve().parent.parent
PROGRESS_LINE = re.compile(r"^- \[([ x])\]\s*(\d+)\s*—\s*(.+)$")


def parse_syllabus() -> list[tuple[str, str]]:
    """Pull (module_number, title) pairs out of README.md's Progress list."""
    readme = (ROOT / "README.md").read_text()
    in_progress_section = False
    entries = []
    for line in readme.splitlines():
        if line.strip() == "## Progress":
            in_progress_section = True
            continue
        if in_progress_section and line.startswith("## "):
            break
        if in_progress_section:
            match = PROGRESS_LINE.match(line.strip())
            if match:
                _, number, title = match.groups()
                entries.append((number, title))
    return entries


def find_module_dir(number: str) -> Path | None:
    matches = list((ROOT / "modules").glob(f"{number}_*"))
    return matches[0] if matches else None


def run_module_tests(module_dir: Path) -> bool | None:
    """True = all passing, False = exists but failing/incomplete, None = no tests yet."""
    if not any(module_dir.glob("test_*.py")):
        return None
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=module_dir,
        capture_output=True,
    )
    return result.returncode == 0


def main() -> None:
    syllabus = parse_syllabus()
    statuses: list[tuple[str, str, Path | None, bool | None]] = []

    for number, title in syllabus:
        module_dir = find_module_dir(number)
        passing = run_module_tests(module_dir) if module_dir else None
        statuses.append((number, title, module_dir, passing))

    done = sum(1 for _, _, _, passing in statuses if passing)
    total = len(statuses)

    if console is None:
        _print_plain(statuses, done, total)
        return

    _print_rich(statuses, done, total)


def _bar(done: int, total: int, width: int = 30) -> str:
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def _print_plain(statuses, done, total) -> None:
    print(f"Progress: {done}/{total} modules complete")
    for number, title, module_dir, passing in statuses:
        if passing is True:
            mark = "[x]"
        elif module_dir is None:
            mark = "[ ] (not built yet)"
        else:
            mark = "[ ]"
        print(f"  {mark} {number} — {title}")
    _print_next_steps_plain(statuses)


def _print_next_steps_plain(statuses) -> None:
    for number, title, module_dir, passing in statuses:
        if passing:
            continue
        if module_dir is None:
            print(f"\nYou're caught up on everything built so far. Module {number} "
                  f"({title}) hasn't been created yet — ask Claude to build it.")
        else:
            print(f"\nResume here: Module {number} — {title}")
            print(f"  cd {module_dir.relative_to(ROOT)}")
            print("  cat LESSON.md   # or open it in an editor")
            print("  pytest")
        return
    print("\nEverything in the syllabus so far is complete. Nice work.")


def _print_rich(statuses, done, total) -> None:
    console.print(f"[bold]{_bar(done, total)}[/bold]  {done}/{total} modules complete")
    console.print()

    for number, title, module_dir, passing in statuses:
        if passing:
            icon, style = ":white_check_mark:", "green"
        elif module_dir is None:
            icon, style = "·", "dim"
        else:
            icon, style = "○", "yellow"
        suffix = " [dim](not built yet)[/dim]" if module_dir is None else ""
        console.print(f"[{style}]{icon} {number} — {title}{suffix}[/{style}]")

    console.print()

    for number, title, module_dir, passing in statuses:
        if passing:
            continue
        if module_dir is None:
            console.print(
                Panel(
                    f"You're caught up on everything built so far.\n"
                    f"Module {number} — {title} hasn't been created yet — "
                    "just say the word and it'll get built next.",
                    title="Caught up",
                    border_style="cyan",
                )
            )
        else:
            rel = module_dir.relative_to(ROOT)
            console.print(
                Panel(
                    f"[bold]Module {number} — {title}[/bold]\n\n"
                    f"  cd {rel}\n"
                    f"  cat LESSON.md   [dim]# or open it in an editor[/dim]\n"
                    f"  pytest",
                    title="Resume here",
                    border_style="cyan",
                )
            )
        return

    console.print(
        Panel(
            "Everything in the syllabus so far is complete. Nice work — "
            "ask for the next module whenever you're ready.",
            title=":tada: All caught up",
            border_style="green",
        )
    )


if __name__ == "__main__":
    main()
