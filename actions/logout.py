"""Logout confirmation actions."""
from actions._common import Point, click_template
import config


def click_logout() -> Point:
    """Return logout click coordinate."""
    return click_template("logout.png", config.FORCE_LOGOUT)
def click_yes() -> Point:
    """Return logout-confirmation click coordinate."""
    return click_template("yes.png", config.FORCE_YES)
