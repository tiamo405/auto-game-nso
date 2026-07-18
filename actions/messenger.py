"""Messenger action."""
from actions._common import Point, click_template
FORCE_MESSENGER: Point | None = None
def click_messenger() -> Point:
    """Return messenger click coordinate."""
    return click_template("messager.png", FORCE_MESSENGER)
