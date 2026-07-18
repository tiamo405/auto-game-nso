"""Screen capture and OpenCV template matching."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import time

import cv2
import mss
import numpy as np

import config

Point = tuple[int, int]


def _capture_screen() -> np.ndarray:
    """Capture all virtual monitors as a BGRA NumPy image."""
    with mss.mss() as capture:
        return np.array(capture.grab(capture.monitors[0]))


def save_failure_screenshot(step: str) -> Path:
    """Save the current screen under logs and return its path."""
    config.LOGS_DIR.mkdir(parents=True, exist_ok=True)
    safe_step = "".join(char if char.isalnum() or char in "-_" else "_" for char in step)
    filename = f"{datetime.now():%Y%m%d_%H%M%S}_{safe_step}.png"
    path = config.LOGS_DIR / filename
    cv2.imwrite(str(path), _capture_screen())
    return path


def _show_debug(screen: np.ndarray, top_left: tuple[int, int], width: int, height: int) -> None:
    """Draw a green match rectangle and refresh the debug preview."""
    preview = screen.copy()
    x, y = top_left
    cv2.rectangle(preview, (x, y), (x + width, y + height), (0, 255, 0, 255), 2)
    cv2.imshow(config.DEBUG_WINDOW_NAME, preview)
    cv2.waitKey(1)


def find_image(
    image_path: str | Path,
    confidence: float = config.CONFIDENCE,
    timeout: float = config.FIND_TIMEOUT_SECONDS,
) -> Point | None:
    """Return a template's screen-center coordinate, or ``None`` after timeout."""
    template = cv2.imread(str(image_path), cv2.IMREAD_UNCHANGED)
    if template is None:
        raise FileNotFoundError(f"Template image not found or unreadable: {image_path}")

    template_bgr = template[:, :, :3] if template.ndim == 3 else template
    mask = template[:, :, 3] if template.ndim == 3 and template.shape[2] == 4 else None
    height, width = template_bgr.shape[:2]
    deadline = time.monotonic() + timeout

    while time.monotonic() < deadline:
        screen = _capture_screen()
        screen_bgr = screen[:, :, :3]
        method = cv2.TM_CCORR_NORMED if mask is not None else cv2.TM_CCOEFF_NORMED
        result = cv2.matchTemplate(screen_bgr, template_bgr, method, mask=mask)
        _, score, _, top_left = cv2.minMaxLoc(result)
        if score >= confidence:
            if config.DEBUG:
                _show_debug(screen, top_left, width, height)
            return (top_left[0] + width // 2, top_left[1] + height // 2)
        if config.DEBUG:
            cv2.imshow(config.DEBUG_WINDOW_NAME, screen)
            cv2.waitKey(1)
        time.sleep(config.RETRY_INTERVAL_SECONDS)
    return None
