import os
import json
import pandas as pd
from glob import glob
from datetime import datetime

RAW_DIR = "../data/raw"
PROCESSED_DIR = "../data/processed"


def load_latest_raw():
    """Load the newest raw JSON file."""
    files = glob(os.path.join(RAW_DIR, "*.json"))
    if not files:
        raise FileNotFoundError("No raw JSON files found.")

    latest_file = max(files, key=os.path.getmtime)
    with open(latest_file, "r") as f:
        data = json.load(f)

    print(f"Loaded raw file: {latest_file}")
    return pd.DataFrame(data)


def transform(df):
    """Example transformation — create percentage change."""
    if "current_price" in df.columns:
        df["returns"] = df["current_price"].pct_change()
    return df


def save_processed(df):
    """Save transformed data to JSON."""
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"crypto_processed_{timestamp}.json"
    filepath = os.path.join(PROCESSED_DIR, filename)

    df.to_json(filepath, orient="records", indent=4)
    print(f"Saved processed file: {filepath}")


def main():
    df = load_latest_raw()
    df = transform(df)
    save_processed(df)


if __name__ == "__main__":
    main()
