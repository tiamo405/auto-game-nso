"""Dedicated reward-receive actions."""
from actions._common import Point, click_template
import config


def click_receive_first() -> Point:
    """Return first receive click coordinate."""
    return click_template("receive.png", config.FORCE_RECEIVE_FIRST)
def click_receive_second() -> Point:
    """Return second receive click coordinate."""
    return click_template("receive.png", config.FORCE_RECEIVE_SECOND)
