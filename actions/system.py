"""System message action."""
from actions._common import Point, click_template
import config


def click_system() -> Point:
    """Return system tab click coordinate."""
    return click_template("system.png", config.FORCE_SYSTEM)
