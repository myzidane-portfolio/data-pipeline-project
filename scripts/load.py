import os
import json
import pandas as pd
from glob import glob
from datetime import datetime

PROCESSED_DIR = "../data/processed"
FINAL_DIR = "../data/final"


def load_latest_processed():
    """Load newest processed JSON file."""
    files = glob(os.path.join(PROCESSED_DIR, "*.json"))
    if not files:
        raise FileNotFoundError("No processed JSON files found.")

    latest_file = max(files, key=os.path.getmtime)
    with open(latest_file, "r") as f:
        data = json.load(f)

    print(f"Loaded processed file: {latest_file}")
    return pd.DataFrame(data)


def final_cleanup(df):
    """Optional cleanup step."""
    return df.dropna()


def save_final(df):
    os.makedirs(FINAL_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"crypto_final_{timestamp}.json"
    filepath = os.path.join(FINAL_DIR, filename)

    df.to_json(filepath, orient="records", indent=4)
    print(f"Saved final file: {filepath}")


def main():
    df = load_latest_processed()
    df = final_cleanup(df)
    save_final(df)


if __name__ == "__main__":
    main()
