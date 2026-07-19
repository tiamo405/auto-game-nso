"""Messenger action."""
from actions._common import Point, click_template
import config


def click_messenger() -> Point:
    """Return messenger click coordinate."""
    return click_template("messager.png", config.FORCE_MESSENGER)
