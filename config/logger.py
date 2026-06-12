import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
LOG_FILE = os.path.join(LOG_DIR, "jarvis.log")

os.makedirs(LOG_DIR, exist_ok=True)

formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=1_000_000,
    backupCount=3,
    encoding="utf-8",
)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger