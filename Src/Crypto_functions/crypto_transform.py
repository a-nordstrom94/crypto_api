import pandas as pd
from pathlib import Path
from .logging_config import logger


def load_raw_data() -> pd.DataFrame:
    data_path = Path(__file__).parent.parent.parent / "Data" / "Raw" / "crypto_data_raw.json"
    try:
        df = pd.read_json(data_path)
        logger.info(f"Raw data loaded from {data_path}")
        return df
    except Exception as e:
        logger.exception("Error loading raw data from file")
        raise


def compute_insights(df: pd.DataFrame) -> dict:
    logger.info("Computing insights from raw data...")
    insights = {}
    # --- top 10 market cap ---
    top_10 = df.sort_values("market_cap", ascending=False).head(10)
    insights["top_10_market_cap"] = top_10

    # --- 24h losers ---
    top_10_loser_24h = df.sort_values("price_change_percentage_24h", ascending=True).head(10)
    insights["top_10_loser_24h"] = top_10_loser_24h

    # --- 24h volatility ratio (high to low) ---
    df["volatility_ratio"] = df["high_24h"] / df["low_24h"]
    top_10_volatile_24h = df.sort_values("volatility_ratio", ascending=False).head(10)
    insights["top_10_volatile_24h"] = top_10_volatile_24h

    # --- Top 10 changes from all time high ---
    top_10_below_ath = df.sort_values("ath_change_percentage", ascending=True).head(10)
    insights["top_10_below_ath"] = top_10_below_ath

    mark_cap_10 = df[df["market_cap_rank"].between(1,10)]
    mark_cap_11_50 = df[df["market_cap_rank"].between(11,50)]
    mark_cap_51_100 = df[df["market_cap_rank"].between(51,100)]
    mark_cap_10_avg = mark_cap_10["price_change_percentage_24h"].mean()
    mark_cap_11_50_avg = mark_cap_11_50["price_change_percentage_24h"].mean()
    mark_cap_51_100_avg = mark_cap_51_100["price_change_percentage_24h"].mean()
    insights["mark_cap_avg_changes"] = {
        "1-10": mark_cap_10_avg,
        "11-50": mark_cap_11_50_avg,
        "51-100": mark_cap_51_100_avg
    }
    logger.info("Insights computation completed.")
    return insights

def save_processed_data(insights: dict):
    output_dir = Path(__file__).parent.parent.parent / "Data" / "Processed"
    output_dir.mkdir(parents=True, exist_ok=True)
    try:
        insights["top_10_market_cap"].to_csv(output_dir / "top_10_market_cap.csv", index=False)
        insights["top_10_loser_24h"].to_csv(output_dir / "top_10_loser_24h.csv", index=False)
        insights["top_10_volatile_24h"].to_csv(output_dir / "top_10_volatile_24h.csv", index=False)
        insights["top_10_below_ath"].to_csv(output_dir / "top_10_below_ath.csv", index=False)
        
        "for loop to write avg changes, key and value pairs (low, med, high)"
        with open(output_dir / "market_cap_avg_changes.txt", 'w') as f:
            for k, v in insights["mark_cap_avg_changes"].items():
                f.write(f"Market Cap Rank {k}: Average 24h Change = {v:.2f}%\n")

        logger.info("Processed data saved to %s", output_dir)
    except Exception as e:
        logger.exception("Error saving processed data: %s", e)
        raise