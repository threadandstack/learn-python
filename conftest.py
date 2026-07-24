"""
Shared pytest hooks for LEARN_PYTHON.

This adds a friendly banner before and after pytest's own output — it never
changes whether tests pass or fail, and never hides pytest's real output
(reading a real traceback is part of the curriculum, not something to skip
past). It only adds a short message around it.

The amount of visual "flourish" tapers off as the module number goes up, on
the theory that you need more hand-holding in module 01 than in module 14.
If `rich` isn't installed for some reason, everything degrades to plain
text rather than breaking.

Rendered output is routed through the terminal reporter's own
`write_raw()` rather than printed straight to stdout. A separate stream
(which is what a bare `Console().print()` uses) can get physically
interleaved with pytest's own buffered writer in the wrong order —
harmless in some terminals, visible as scrambled ordering in others.
Writing through the same writer pytest itself uses avoids that entirely.
"""

from __future__ import annotations

import io
import re
from pathlib import Path

import pytest

try:
    from rich.console import Console

    _RICH = True
except ImportError:
    _RICH = False


def _render(renderable, width: int = 100) -> str:
    """Render a Rich renderable (or markup string) to an ANSI string."""
    buf = io.StringIO()
    Console(file=buf, force_terminal=True, width=width, color_system="standard").print(renderable)
    return buf.getvalue()


def _emit(terminalreporter, renderable) -> None:
    if terminalreporter is None or not _RICH:
        return
    width = getattr(terminalreporter, "_tw", None)
    width = width.fullwidth if width is not None else 100
    terminalreporter.write_raw(_render(renderable, width=min(width, 100)))


def _current_module() -> tuple[int | None, str | None]:
    """Best-effort: which module folder is pytest running from?"""
    match = re.match(r"^(\d+)_(.+)$", Path.cwd().name)
    if match:
        return int(match.group(1)), match.group(2).replace("_", " ")
    return None, None


def _flourish_level(module_num: int | None) -> str:
    # Thresholds track the syllabus phases in README.md: Phase 1
    # (Foundations, 00-05) gets the most hand-holding, Phase 4 (trainee-dev
    # habits, 16-18) the least.
    if module_num is None:
        return "medium"
    if module_num <= 5:
        return "high"
    if module_num <= 15:
        return "medium"
    return "low"


def pytest_sessionstart(session):
    terminalreporter = session.config.pluginmanager.get_plugin("terminalreporter")
    num, name = _current_module()
    level = _flourish_level(num)

    if not _RICH:
        return

    from rich.panel import Panel

    if level == "high":
        title = f"Module {num:02d} — {name.title()}" if num is not None else "LEARN_PYTHON"
        _emit(
            terminalreporter,
            Panel(
                "[bold]Let's go.[/bold] Run the tests, read what they tell "
                "you, fix, rerun. No rush — the tests aren't timed.",
                title=title,
                border_style="cyan",
            ),
        )
    elif level == "medium":
        label = f"Module {num:02d}" if num is not None else "LEARN_PYTHON"
        _emit(terminalreporter, f"[bold cyan]▸ {label}[/bold cyan] running checks…")
    # level == "low": say nothing here, let pytest's own output lead.


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    # TerminalReporter's own pytest_sessionfinish is itself a *wrapper*
    # hook: it does `result = yield` first (running every other hookimpl),
    # and only prints FAILURES/short-summary/the final "N passed in Xs"
    # line *after* that yield returns. To land truly last, we also need to
    # be the *outermost* wrapper, i.e. the first one pluggy calls — hence
    # tryfirst=True — so that our own `yield` is what triggers the
    # reporter's wrapper (and everything else), and our code below only
    # resumes once that's all completely unwound.
    result = yield
    terminalreporter = session.config.pluginmanager.get_plugin("terminalreporter")
    if terminalreporter is None:
        return result

    num, _ = _current_module()
    level = _flourish_level(num)
    stats = terminalreporter.stats
    passed = len(stats.get("passed", []))
    not_passed = len(stats.get("failed", [])) + len(stats.get("error", []))
    has_solutions = (Path.cwd() / "solutions").is_dir()

    if not _RICH:
        if not_passed:
            terminalreporter.write_line(
                "Not there yet — read the failure above closely, it usually "
                "says exactly what's wrong."
            )
        else:
            terminalreporter.write_line("All green. Nice work.")
        return result

    from rich.panel import Panel

    if not_passed:
        # Same supportive tone at every level, on purpose — never punitive.
        if level == "high":
            _emit(
                terminalreporter,
                Panel(
                    f"[bold yellow]{passed} passed, {not_passed} not yet.[/bold yellow]\n"
                    "Completely normal for a first pass. Scroll up to the "
                    "failure — pytest tells you the exact line, plus what it "
                    "expected vs. what it got. Fix one thing, rerun, repeat.",
                    title="Almost there",
                    border_style="yellow",
                ),
            )
        else:
            _emit(
                terminalreporter,
                f"[yellow]{passed} passed, {not_passed} to go[/yellow] — "
                "check the failure above, fix, rerun.",
            )
        return result

    # Everything passed.
    next_step = (
        "Peek at solutions/solution.py and compare notes, then move on whenever you're ready."
        if has_solutions
        else "Move on whenever you're ready."
    )
    if level == "high":
        _emit(
            terminalreporter,
            Panel(
                f"[bold green]:tada: All {passed} passed![/bold green]\n{next_step}",
                title="Nice work",
                border_style="green",
            ),
        )
    elif level == "medium":
        _emit(
            terminalreporter,
            f"[bold green]:white_check_mark: {passed} passed.[/bold green] On to the next one.",
        )
    else:
        _emit(terminalreporter, f"[green]{passed} passed.[/green]")

    return result
