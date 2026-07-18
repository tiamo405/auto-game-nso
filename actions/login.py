"""Login form click actions."""
from actions._common import Point, click_template
FORCE_USERNAME: Point | None = None
FORCE_PASSWORD: Point | None = None
FORCE_OK: Point | None = None
FORCE_LOGIN: Point | None = None
def click_username() -> Point:
    """Return click coordinate for the username field."""
    return click_template("username.png", FORCE_USERNAME)
def click_password() -> Point:
    """Return click coordinate for the password field."""
    return click_template("password.png", FORCE_PASSWORD)
def click_ok() -> Point:
    """Return click coordinate for the form confirmation button."""
    return click_template("ok.png", FORCE_OK)
def click_login() -> Point:
    """Return click coordinate for the login button."""
    return click_template("login.png", FORCE_LOGIN)
