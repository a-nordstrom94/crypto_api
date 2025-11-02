import requests
import json
from pathlib import Path
from .logging_config import logger

def fetch_crypto_data():
    """
    Fetch cryptocurrency data from a public API and save it as a JSON file.
    Returns the fetched data if successful, otherwise None.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        logger.info("Succesffully fetched %d records from the API", len(data))
        return data
    except requests.RequestException as e:
        logger.error("Error fetching data from API: %s", e)
        return None

def save_raw_data(data):
    """
    Save the fetched data to a JSON file.
    """
    output_dir = Path(__file__).parent.parent.parent / "Data"/ "Raw"
    output_dir.mkdir(exist_ok=True)  # create folder if it doesn't exist

    data_path = output_dir / "crypto_data_raw.json"
    try:
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logger.info("Raw data saved to %s", data_path)
    except Exception as e:
        logger.exception("Error saving raw data to file: %s", e)
        raise