"""Small, consistently formatted console logger."""

import logging


def get_logger(name: str = "game_automation") -> logging.Logger:
    """Return a console logger without adding duplicate handlers."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
    return logger
