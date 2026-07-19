"""Keyboard and clipboard input helpers."""

import pydirectinput
import pyperclip

import config


def ctrl_a() -> None:
    """Select all text in the focused input."""
    _ctrl_key("a")


def backspace() -> None:
    """Delete the selected text."""
    pydirectinput.press("backspace")


def press_enter() -> None:
    """Press Enter."""
    pydirectinput.press("enter")


def press_tab() -> None:
    """Press Tab."""
    pydirectinput.press("tab")


def _ctrl_key(key: str) -> None:
    """Send a Ctrl+key combination without relying on pydirectinput.hotkey."""
    pydirectinput.keyDown("ctrl")
    try:
        pydirectinput.press(key)
    finally:
        pydirectinput.keyUp("ctrl")


def type_text(text: str) -> None:
    """Replace focused text using the configured Unity-compatible input method."""
    ctrl_a()
    backspace()
    value = str(text)
    if config.TEXT_INPUT_METHOD == "direct":
        print("dang typing bang ", config.TEXT_INPUT_METHOD)
        pydirectinput.write(value, interval=config.TEXT_TYPING_INTERVAL_SECONDS)
    elif config.TEXT_INPUT_METHOD == "clipboard":
        print("dang typing bang clipboard")
        pyperclip.copy(value)
        _ctrl_key("v")
    else:
        raise ValueError(
            "TEXT_INPUT_METHOD must be 'direct' or 'clipboard', "
            f"not {config.TEXT_INPUT_METHOD!r}"
        )
