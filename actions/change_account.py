"""Change-account screen action."""
from actions._common import Point, click_template
FORCE_CHANGE_ACCOUNT: Point | None = None
def click_change_account() -> Point:
    """Return click coordinate; set FORCE_CHANGE_ACCOUNT to bypass matching."""
    return click_template("change-account.png", FORCE_CHANGE_ACCOUNT)
