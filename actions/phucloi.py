"""Phúc lợi (phucloi) actions.
"""
from actions._common import Point, click_template
import config


def click_icon_phucloi() -> Point:
    """Return phúc lợi icon click coordinate."""
    return click_template("icon-phucloi.png", config.FORCE_ICON_PHUCLOI)


def click_goiqua() -> Point:
    """Return gói quà click coordinate."""
    return click_template("goi-qua.png", config.FORCE_GOIQUA)


def click_tanthu() -> Point:
    """Return Tân thủ (newbie) gift group click coordinate."""
    return click_template("tan-thu.png", config.FORCE_TAN_THU)


def click_nhanthuong_tanthu() -> Point:
    """Return receive/newbie reward click coordinate."""
    return click_template("nhanthuong-tanthu.png", config.FORCE_NHANTHUONG_TANTHU)


def click_dong() -> Point:
    """Return close (đóng) button click coordinate."""
    return click_template("dong.png", config.FORCE_DONG)

def click_ok_nhanquatanthu() -> Point:
    """Return OK button click coordinate after receiving newbie gift."""
    return click_template("ok-nhanquatanthu.png", config.FORCE_OK_NHANQUATANTHU)
