"""Dedicated reward-receive actions."""
from actions._common import Point, click_template
FORCE_RECEIVE_FIRST: Point | None = None
FORCE_RECEIVE_SECOND: Point | None = None
def click_receive_first() -> Point:
    """Return first receive click coordinate."""
    return click_template("receive.png", FORCE_RECEIVE_FIRST)
def click_receive_second() -> Point:
    """Return second receive click coordinate."""
    return click_template("receive.png", FORCE_RECEIVE_SECOND)
