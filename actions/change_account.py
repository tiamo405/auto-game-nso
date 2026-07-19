"""Change-account screen action."""
from actions._common import Point, click_template
import config


def click_change_account() -> Point:
    """Return click coordinate; set FORCE_CHANGE_ACCOUNT to bypass matching."""
    return click_template("change-account.png", config.FORCE_CHANGE_ACCOUNT)
