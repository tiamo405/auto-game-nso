"""Record Windows cursor coordinates whenever the left mouse button is clicked.

Run with ``python capture_mouse_position.py`` and stop with Ctrl+C.
"""

from __future__ import annotations

import ctypes
from ctypes import wintypes
from datetime import datetime
from pathlib import Path
import time


BASE_DIR = Path(__file__).resolve().parent
LOG_PATH = BASE_DIR / "logs" / "mouse_positions.log"
POLL_INTERVAL_SECONDS = 0.02
VK_LBUTTON = 0x01


class Point(ctypes.Structure):
    """Windows POINT structure used by GetCursorPos."""

    _fields_ = [("x", wintypes.LONG), ("y", wintypes.LONG)]


USER32 = ctypes.WinDLL("user32", use_last_error=True)
USER32.GetCursorPos.argtypes = [ctypes.POINTER(Point)]
USER32.GetCursorPos.restype = wintypes.BOOL
USER32.GetAsyncKeyState.argtypes = [wintypes.INT]
USER32.GetAsyncKeyState.restype = wintypes.SHORT


def get_cursor_position() -> tuple[int, int]:
    """Return the current cursor position in screen coordinates."""
    point = Point()
    if not USER32.GetCursorPos(ctypes.byref(point)):
        raise ctypes.WinError(ctypes.get_last_error())
    return point.x, point.y


def is_left_button_down() -> bool:
    """Return whether the physical left mouse button is currently held."""
    return bool(USER32.GetAsyncKeyState(VK_LBUTTON) & 0x8000)


def record_click(x: int, y: int) -> None:
    """Append one click coordinate to the log and print it."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    message = f"{datetime.now():%Y-%m-%d %H:%M:%S}  ({x}, {y})"
    with LOG_PATH.open("a", encoding="utf-8") as log_file:
        log_file.write(f"{message}\n")
    print(message, flush=True)


def main() -> None:
    """Monitor left-button down transitions until the user presses Ctrl+C."""
    print("Click chuột trái để lấy tọa độ. Nhấn Ctrl+C để dừng.")
    print(f"Log: {LOG_PATH}")
    was_down = False
    try:
        while True:
            is_down = is_left_button_down()
            if is_down and not was_down:
                record_click(*get_cursor_position())
            was_down = is_down
            time.sleep(POLL_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nĐã dừng ghi tọa độ.")


if __name__ == "__main__":
    main()
