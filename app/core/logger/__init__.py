import logging
import logging.config
from functools import lru_cache


@lru_cache
def get_logger(name: str):
    logger = logging.getLogger(name)
    logging.config.dictConfig(LOGGING_CONFIG)
    return logger


TRACE = "INFO"
LOG_LEVEL = TRACE

LOG_FORMAT = "{levelname} | {asctime} | {name} | {filename}:{lineno} |  {message}"
DATE_TIME_FORMAT_ISO_8601 = "%Y-%m-%dT%H:%M:%S.%fZ"  # ISO 8601
DATE_TIME_FORMAT_WITHOUT_MICROSECONDS = "%Y-%m-%dT%H:%M:%SZ"

LOGGING_CONFIG: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default_formatter": {
            "format": LOG_FORMAT,
            "style": "{",
            "datefmt": DATE_TIME_FORMAT_WITHOUT_MICROSECONDS,
            "validate": True,  # 🤷
        }
    },
    "filters": {
        "warnings_and_below": {
            "()": "app.core.logger.filters.filter_maker",
            "level": "WARNING"
        }
    },
    "handlers": {
        "default_handler": {
            "class": "logging.StreamHandler",
            "level": LOG_LEVEL,
            "formatter": "default_formatter",
            "stream": "ext://sys.stdout",
            "filters": ["warnings_and_below"]
        },
        "error_console_handler": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "default_formatter",
            "stream": "ext://sys.stderr"
        },

    },
    "root": {"level": LOG_LEVEL, "handlers": ["default_handler", "error_console_handler"]}
}

if __name__ == "__main__":
    logger = get_logger("test_logger")
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
