"""DirectInput mouse operations for Unity games."""

from typing import TypeAlias

import pydirectinput

import config

Point: TypeAlias = tuple[int, int]
pydirectinput.PAUSE = config.CLICK_PAUSE_SECONDS


def click_point(x: int, y: int) -> None:
    """Click one screen coordinate through DirectInput."""
    pydirectinput.click(x=x, y=y)
