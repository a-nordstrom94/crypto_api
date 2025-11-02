import logging
from pathlib import Path

# Create Logs directory
repo_root = Path(__file__).resolve().parents[2]
log_dir = repo_root / "Logs"
log_dir.mkdir(exist_ok=True)

# Log file path
log_file = log_dir / "pipeline.log"

# Create logger
logger = logging.getLogger("crypto_pipeline")
logger.setLevel(logging.INFO)

# Remove existing handlers to prevent duplicates
if logger.hasHandlers():
    logger.handlers.clear()

# File handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)
