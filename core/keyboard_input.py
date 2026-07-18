"""Keyboard and clipboard input helpers."""

import pydirectinput
import pyperclip


def ctrl_a() -> None:
    """Select all text in the focused input."""
    pydirectinput.hotkey("ctrl", "a")


def backspace() -> None:
    """Delete the selected text."""
    pydirectinput.press("backspace")


def press_enter() -> None:
    """Press Enter."""
    pydirectinput.press("enter")


def press_tab() -> None:
    """Press Tab."""
    pydirectinput.press("tab")


def type_text(text: str) -> None:
    """Replace focused text through clipboard paste, preserving Unicode input."""
    pyperclip.copy(str(text))
    ctrl_a()
    backspace()
    pydirectinput.hotkey("ctrl", "v")
