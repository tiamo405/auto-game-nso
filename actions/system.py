"""System message action."""
from actions._common import Point, click_template
FORCE_SYSTEM: Point | None = None
def click_system() -> Point:
    """Return system tab click coordinate."""
    return click_template("system.png", FORCE_SYSTEM)
