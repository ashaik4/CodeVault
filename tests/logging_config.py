# tests/logging_config.py
import logging

def configure_logging():
    """Set up logging for the test suite."""
    logging.basicConfig(
        level=logging.INFO,  # Set the log level
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log format
    )
    logger = logging.getLogger("tests")  # Create a logger for the test suite
    return logger