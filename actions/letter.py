"""Dedicated letter actions."""
from actions._common import Point, click_template
import config


def click_icon_letter() -> Point:
    """Return mail-icon click coordinate."""
    return click_template("icon-letter.png", config.FORCE_ICON_LETTER)
def click_letter_first() -> Point:
    """Return first letter click coordinate."""
    return click_template("letter.png", config.FORCE_LETTER_FIRST)
def click_letter_second() -> Point:
    """Return second letter click coordinate."""
    return click_template("letter.png", config.FORCE_LETTER_SECOND)
