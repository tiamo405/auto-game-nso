"""Dedicated menu actions (same template, independent overrides)."""
from actions._common import Point, click_template
FORCE_MENU_FIRST: Point | None = None
FORCE_MENU_SECOND: Point | None = None
def click_menu_first() -> Point:
    """Return first menu click coordinate."""
    return click_template("menu.png", FORCE_MENU_FIRST)
def click_menu_second() -> Point:
    """Return second menu click coordinate."""
    return click_template("menu.png", FORCE_MENU_SECOND)
