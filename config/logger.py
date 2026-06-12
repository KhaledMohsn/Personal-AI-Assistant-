import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)-15s | %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(os.path.join(LOG_DIR, "jarvis.log"), maxBytes=1_000_000, backupCount=3, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)