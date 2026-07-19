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


def clear_focused_text() -> None:
    """Clear the focused field only when the configured method permits it."""
    if config.TEXT_CLEAR_METHOD == "none":
        return
    if config.TEXT_CLEAR_METHOD == "right_backspace":
        pydirectinput.press("right", presses=config.MAX_LEN_USER, interval=0)
        pydirectinput.press("backspace", presses=config.MAX_LEN_USER, interval=0)
        return
    if config.TEXT_CLEAR_METHOD == "home_delete":
        pydirectinput.press("home")
        pydirectinput.press(
            "delete", presses=config.MAX_LEN_USER, interval=0
        )
        return
    if config.TEXT_CLEAR_METHOD == "ctrl_a_backspace":
        ctrl_a()
        backspace()
        return
    raise ValueError(
        "TEXT_CLEAR_METHOD must be 'none', 'right_backspace', 'home_delete', "
        "or 'ctrl_a_backspace', "
        f"not {config.TEXT_CLEAR_METHOD!r}"
    )


def type_text(text: str) -> None:
    """Replace focused text using the configured Unity-compatible input method."""
    clear_focused_text()
    value = str(text)
    if config.TEXT_INPUT_METHOD == "direct":
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
