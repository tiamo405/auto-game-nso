"""Dedicated letter actions."""
from actions._common import Point, click_template
import config

def click_icon_letter_v2() -> Point:
    """Return mail-icon click coordinate."""
    return click_template("icon-letter.png", config.FORCE_ICON_LETTER_V2)
