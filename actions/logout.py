"""Logout confirmation actions."""
from actions._common import Point, click_template
FORCE_LOGOUT: Point | None = None
FORCE_YES: Point | None = None
def click_logout() -> Point:
    """Return logout click coordinate."""
    return click_template("logout.png", FORCE_LOGOUT)
def click_yes() -> Point:
    """Return logout-confirmation click coordinate."""
    return click_template("yes.png", FORCE_YES)
