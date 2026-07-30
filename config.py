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

# Hold duration used only for Logout and its Yes confirmation. Some Unity UI
# controls register this more reliably than an instant click.
LOGOUT_CLICK_HOLD_SECONDS = 1

# Unity UI fields can need a moment to receive focus before Ctrl+V is sent.
INPUT_FIELD_FOCUS_WAIT = 0.75
TEXT_INPUT_WAIT = 0.50

# Unity input fields sometimes ignore clipboard paste.  Use "direct" to send
# individual DirectInput keystrokes; change to "clipboard" only if Ctrl+V works
# reliably in your version of the game.
TEXT_INPUT_METHOD = "direct"
TEXT_TYPING_INTERVAL_SECONDS = 0.01

# Some Unity fields reject Ctrl+A and Home.  "right_backspace" moves the text
# cursor right to the end, then deletes old text without Ctrl+A or Home.
# This maximum applies to both username and password fields.
TEXT_CLEAR_METHOD = "right_backspace"
MAX_LEN_USER = 16

# max letter
MAX_LETTER = 10

# Fixed click coordinates.  Set a value to (x, y) to click that position, or
# set it to None to use OpenCV template matching for only that action.
FORCE_CHANGE_ACCOUNT = (742, 388)
FORCE_USERNAME = (677, 345)
FORCE_PASSWORD = (660, 425)
FORCE_OK = (1105, 627)
FORCE_LOGIN = (696, 310)
FORCE_CHARACTER = (516, 369)
FORCE_ICON_LETTER_V2 = (530, 523)
FORCE_LETTER_FIRST = (577, 123)
FORCE_RECEIVE_FIRST = (566, 595)
FORCE_MENU_FIRST = (1005, 159)
FORCE_MENU_SECOND = None
FORCE_MESSENGER = None
FORCE_SYSTEM = None
FORCE_ICON_LETTER = None
FORCE_LETTER_SECOND = None
FORCE_RECEIVE_SECOND = None
FORCE_LOGOUT = (1009, 600)
FORCE_YES = (605, 630)

FORCE_ICON_PHUCLOI = None
FORCE_GOIQUA = None
FORCE_TAN_THU = None
FORCE_NHANTHUONG_TANTHU = None
FORCE_OK_NHANQUATANTHU = None
FORCE_DONG = None

# Workflow delays. Adjust these if the game or connection needs more time.
CHANGE_ACCOUNT_WAIT = 0
LOGIN_FORM_WAIT = 2
LOGIN_WAIT = 5
CHARACTER_WAIT = 3
MENU_WAIT = 1
MESSENGER_WAIT = 2
SYSTEM_WAIT = 2
ICON_LETTER_WAIT = 1
LETTER_WAIT = 2
RECEIVE_WAIT = 0.5
LOGOUT_WAIT = 5
