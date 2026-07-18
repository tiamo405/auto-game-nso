"""Central configuration for the game automation tool."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "imgs"
LOGS_DIR = BASE_DIR / "logs"
ACCOUNTS_FILE = BASE_DIR / "account.csv"

CONFIDENCE = 0.90
RETRY_INTERVAL_SECONDS = 0.5
FIND_TIMEOUT_SECONDS = 20.0

# Set to True to show the captured screen and a green box around each match.
DEBUG = False
DEBUG_WINDOW_NAME = "Unity Game Automation Debug"

# Time to let the UI react after a DirectInput click.
CLICK_PAUSE_SECONDS = 0.10

# Workflow delays. Adjust these if the game or connection needs more time.
CHANGE_ACCOUNT_WAIT = 5
LOGIN_FORM_WAIT = 5
LOGIN_WAIT = 30
CHARACTER_WAIT = 30
MENU_WAIT = 10
MESSENGER_WAIT = 10
SYSTEM_WAIT = 10
ICON_LETTER_WAIT = 10
LETTER_WAIT = 10
RECEIVE_WAIT = 10
LOGOUT_WAIT = 15
