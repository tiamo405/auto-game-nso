"""DirectInput mouse operations for Unity games."""

from typing import TypeAlias
import time

import pydirectinput

import config

Point: TypeAlias = tuple[int, int]
pydirectinput.PAUSE = config.CLICK_PAUSE_SECONDS


def click_point(x: int, y: int) -> None:
    """Click one screen coordinate through DirectInput."""
    pydirectinput.click(x=x, y=y)


def click_point_hold(x: int, y: int, hold_seconds: float) -> None:
    """Hold and release the left mouse button at a screen coordinate."""
    pydirectinput.mouseDown(x=x, y=y)
    try:
        time.sleep(hold_seconds)
    finally:
        pydirectinput.mouseUp(x=x, y=y)
