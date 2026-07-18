"""Character-selection action."""
from actions._common import Point, click_template
FORCE_CHARACTER: Point | None = None
def click_character() -> Point:
    """Return click coordinate for the character tile."""
    return click_template("character.png", FORCE_CHARACTER)
