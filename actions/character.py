"""Character-selection action."""
from actions._common import Point, click_template
import config


def click_character() -> Point:
    """Return click coordinate for the character tile."""
    return click_template("character.png", config.FORCE_CHARACTER)
