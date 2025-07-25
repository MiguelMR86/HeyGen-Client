import logging

from colorlog import ColoredFormatter


def setup_logging(level=logging.DEBUG):
    """
    Set up colored logging.
    """
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s %(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            "DEBUG": "cyan",
            "INFO": "white",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
        secondary_log_colors={},
        style="%",
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(level)
