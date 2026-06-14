import logging
import sys


def setup_logger():
    """Function to setup a logger with the specified name, log file, and logging level."""
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler = logging.FileHandler("log_file.log")
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter("%(levelname)s | %(message)s | %(asctime)s")
    )
    logger.addHandler(console_handler)

    return logger
