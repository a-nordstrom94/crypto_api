"""
Main entry point for the Crypto Data Pipeline.
Orchestrates the end-to-end process:
1. Fetch crypto market data from API
2. Save raw data
3. Load and transform data
4. Save processed outputs
"""

from .Crypto_functions.logging_config import logger

from .Crypto_functions import (
    fetch_crypto_data, 
    save_raw_data, 
    load_raw_data, 
    compute_insights, 
    save_processed_data
)

def main():
    try:
        logger.info("Starting Crypto Data Pipeline")

        # Step 1: Fetch data from API
        data = fetch_crypto_data()
        if data is None:
            logger.error("Failed to fetch data. Exiting.")
            return
        else:
            logger.info("Data fetched successfully." \
            " Number of records fetched: %d", len(data))

        # Step 2: Save raw data
        save_raw_data(data)
        logger.info("Raw data saved successfully.")

        # Step 3: Load and transform data
        df = load_raw_data()
        insights = compute_insights(df)
        logger.info("Data transformation complete.")

        # Step 4: Save processed outputs
        save_processed_data(insights)
        logger.info("Processed data saved successfully.")

        logger.info("Crypto Data Pipeline completed successfully.")
    except Exception as e:
        logger.exception("An error occurred during the pipeline execution: %s", e)

if __name__ == "__main__":
    main()