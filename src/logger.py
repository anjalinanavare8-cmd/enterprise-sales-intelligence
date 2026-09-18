import logging
import os


# Create logs folder if it does not exist
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/system.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_error(error):
    """Save an error message to the system log."""
    logging.error(str(error))
