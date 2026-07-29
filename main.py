"""Run the Unity game account-reward automation.

Open and focus the game yourself, then run ``python main.py`` on Windows.
Press F8 to pause/resume and Escape to stop safely between operations.
"""

from __future__ import annotations

from dataclasses import dataclass
import sys
import threading
import time
from typing import Callable

import keyboard
import pandas as pd

import config
from actions.change_account import click_change_account
from actions.character import click_character
from actions.letter import click_icon_letter, click_letter_first, click_letter_second
from actions.letter_v2 import click_icon_letter_v2
from actions.login import click_login, click_ok, click_password, click_username
from actions.logout import click_logout, click_yes
from actions.menu import click_menu_first, click_menu_second
from actions.messenger import click_messenger
from actions.receive import click_receive_first, click_receive_second
from actions.system import click_system
from actions.phucloi import (
    click_icon_phucloi,
    click_goiqua,
    click_tanthu,
    click_nhanthuong_tanthu,
    click_dong,
    click_ok_nhanquatanthu
)
from core.image import save_failure_screenshot
from core.keyboard_input import type_text
from core.logger import get_logger

LOGGER = get_logger()


class AutomationStopped(Exception):
    """Raised when the user presses Escape."""


class RunControls:
    """Thread-safe pause and stop state driven by global hotkeys."""

    def __init__(self) -> None:
        self._paused = threading.Event()
        self._stopped = threading.Event()

    def toggle_pause(self) -> None:
        if self._paused.is_set():
            self._paused.clear()
            LOGGER.info("Resumed.")
        else:
            self._paused.set()
            LOGGER.info("Paused. Press F8 to resume.")

    def stop(self) -> None:
        self._stopped.set()
        LOGGER.info("Exit requested.")

    def checkpoint(self) -> None:
        """Block while paused and stop promptly when requested."""
        while self._paused.is_set():
            if self._stopped.is_set():
                raise AutomationStopped
            time.sleep(0.1)
        if self._stopped.is_set():
            raise AutomationStopped

    def wait(self, seconds: float) -> None:
        """Wait without making pause/exit hotkeys unresponsive."""
        deadline = time.monotonic() + seconds
        while time.monotonic() < deadline:
            self.checkpoint()
            time.sleep(min(0.1, deadline - time.monotonic()))


@dataclass(frozen=True)
class Account:
    """One row from account.csv."""

    username: str
    password: str


def read_accounts() -> list[Account]:
    """Load and validate username/password records from the configured CSV."""
    frame = pd.read_csv(config.ACCOUNTS_FILE, dtype=str, encoding="utf-8-sig").fillna("")
    required = {"username", "password"}
    if not required.issubset(frame.columns):
        raise ValueError("account.csv must contain exactly the columns: username,password")
    accounts = [Account(row.username, row.password) for row in frame.itertuples(index=False)]
    if not accounts:
        raise ValueError("account.csv contains no accounts")
    return accounts


def perform(step: str, action: Callable[[], object], controls: RunControls) -> None:
    """Perform one action and retain its underlying error in the console log."""
    controls.checkpoint()
    try:
        action()
    except AutomationStopped:
        raise
    except Exception as exc:
        LOGGER.exception("Underlying error during step: %s", step)
        raise RuntimeError(step) from exc


def process_account(account: Account, number: int, controls: RunControls, version = "v2", func=None) -> None:
    """Execute the requested reward collection workflow for one account."""
    LOGGER.info("\n[Account %s username %s : ]", number, account.username)

    perform("Click Change Account", click_change_account, controls)
    LOGGER.info("Click Change Account")
    controls.wait(config.CHANGE_ACCOUNT_WAIT)

    perform("Click Username", click_username, controls)
    controls.wait(config.INPUT_FIELD_FOCUS_WAIT)

    perform("Enter Username", lambda: type_text(account.username), controls)
    LOGGER.info("Username entered")
    controls.wait(config.TEXT_INPUT_WAIT)

    perform("Click Password", click_password, controls)
    controls.wait(config.INPUT_FIELD_FOCUS_WAIT)

    perform("Enter Password", lambda: type_text(account.password), controls)
    LOGGER.info("Password entered")
    controls.wait(config.TEXT_INPUT_WAIT)

    perform("Click OK", click_ok, controls)
    controls.wait(config.LOGIN_FORM_WAIT)

    perform("Click Login", click_login, controls)
    LOGGER.info("Login clicked")
    controls.wait(config.LOGIN_WAIT)

    perform("Click Character", click_character, controls)
    LOGGER.info("Character selected")
    controls.wait(config.CHARACTER_WAIT)
    if version == "v1" and "get_letter" in func:
        # mở menu
        perform("Open Menu", click_menu_first, controls)
        LOGGER.info("Menu opened")
        controls.wait(config.MENU_WAIT)

        # mở messenger
        perform("Open Messenger", click_messenger, controls)
        LOGGER.info("Messenger opened")
        controls.wait(config.MESSENGER_WAIT)

        # mở system
        perform("Select System", click_system, controls)
        LOGGER.info("System selected")
        controls.wait(config.SYSTEM_WAIT)

        # ấn icon letter
        perform("Click Icon Letter", click_icon_letter, controls)
        LOGGER.info("Icon letter opened")
        controls.wait(config.ICON_LETTER_WAIT)
        
        # ấn letter 1 và nhận thưởng
        perform("Click Letter 1", click_letter_first, controls)
        controls.wait(config.LETTER_WAIT)
        perform("Receive Reward 1", click_receive_first, controls)
        LOGGER.info("Receive reward 1")
        controls.wait(config.RECEIVE_WAIT)

        # ấn letter 2 và nhận thưởng
        perform("Click Letter 2", click_letter_second, controls)
        controls.wait(config.LETTER_WAIT)
        perform("Receive Reward 2", click_receive_second, controls)
        LOGGER.info("Receive reward 2")
        controls.wait(config.RECEIVE_WAIT)
    elif version == "v2" and "get_letter" in func:
        # ấn icon letter v2
        perform("Click Icon Letter v2", click_icon_letter_v2, controls)
        LOGGER.info("Icon letter opened")
        controls.wait(config.ICON_LETTER_WAIT)

        # ấn letter 1 -> ấn nhận -> ấn nhận là nhận letter 2 luôn
        perform("Click Letter 1", click_letter_first, controls)
        controls.wait(config.LETTER_WAIT)
        for i in range(1, config.MAX_LETTER+1):
            # ấn nhận thưởng thu i
            perform(f"Receive Reward {i}", click_receive_first, controls)
            LOGGER.info(f"Receive reward {i}")
            controls.wait(config.RECEIVE_WAIT)
    controls.wait(2)

    if "phucloi" in func:
        # ấn icon phucloi
        perform("Click Icon Phuc Loi", click_icon_phucloi, controls)
        controls.wait(1)
        # ấn gói quà
        perform("Click Goi Qua", click_goiqua, controls)
        controls.wait(1)
        # ấn Tân thủ
        perform("Click Tan Thu", click_tanthu, controls)
        controls.wait(1)
        # ấn nhận thưởng
        perform("Receive Reward", click_nhanthuong_tanthu, controls)
        controls.wait(1)
        # ấn ok
        perform("Click OK", click_ok_nhanquatanthu, controls)
        controls.wait(1)
        # ấn đóng
        perform("Click Dong", click_dong, controls)
        controls.wait(2)
    
    # ấn logout
    LOGGER.info("Logout process - press menu 1 view screen menu")
    perform("Open Menu (logout)", click_menu_first, controls)
    controls.wait(config.MENU_WAIT)
    
    LOGGER.info("chon nut logout")
    perform("Click Logout", click_logout, controls)
    controls.wait(2)

    LOGGER.info("Logout process - confirm logout")
    perform("Confirm Logout", click_yes, controls)
    controls.wait(config.LOGOUT_WAIT)
    
    LOGGER.info("Logout success")


def main() -> int:
    """Install controls, process accounts, and report failures with screenshots."""
    controls = RunControls()
    keyboard.add_hotkey("f8", controls.toggle_pause)
    keyboard.add_hotkey("esc", controls.stop)
    LOGGER.info(
        "F8 pauses/resumes; Escape exits. Keep the Unity game open and visible."
    )
    version = "v2"
    func = ["get_letter", "phucloi"]
    try:
        for index, account in enumerate(read_accounts(), start=1):
            process_account(account, index, controls, version, func)
    except AutomationStopped:
        LOGGER.info("Automation stopped by user.")
        return 0
    except Exception as exc:
        step = str(exc)
        screenshot = save_failure_screenshot(step)
        LOGGER.error("FAILED: %s. Screenshot saved to %s", step, screenshot)
        return 1
    finally:
        keyboard.unhook_all_hotkeys()
        if config.DEBUG:
            import cv2
            cv2.destroyAllWindows()
    LOGGER.info("All accounts completed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
