"""Logout confirmation actions."""
from actions._common import Point, click_template
import config


def click_logout() -> Point:
    """Hold-click logout and return its coordinate."""
    return click_template(
        "logout.png",
        config.FORCE_LOGOUT,
        hold_seconds=config.LOGOUT_CLICK_HOLD_SECONDS,
    )


def click_yes() -> Point:
    """Hold-click logout confirmation and return its coordinate."""
    return click_template(
        "yes.png",
        config.FORCE_YES,
        hold_seconds=config.LOGOUT_CLICK_HOLD_SECONDS,
    )
