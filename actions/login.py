"""Login form click actions."""
from actions._common import Point, click_template
import config


def click_username() -> Point:
    """Return click coordinate for the username field."""
    return click_template("username.png", config.FORCE_USERNAME)
def click_password() -> Point:
    """Return click coordinate for the password field."""
    return click_template("password.png", config.FORCE_PASSWORD)
def click_ok() -> Point:
    """Return click coordinate for the form confirmation button."""
    return click_template("ok.png", config.FORCE_OK)
def click_login() -> Point:
    """Return click coordinate for the login button."""
    return click_template("login.png", config.FORCE_LOGIN)
