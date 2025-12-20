import requests
import json
import os
from datetime import datetime


def extract_crypto_data():
    URL = "https://api.coingecko.com/api/v3/coins/markets"
    PARAMS = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    print("📡 Requesting cryptocurrency market data...")
    response = requests.get(URL, params=PARAMS)

    if response.status_code == 200:
        data = response.json()
        os.makedirs("../data/raw", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"crypto_raw_{timestamp}.json"
        filepath = f"../data/raw/{filename}"

        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

        print(f"✅ Data extraction complete! Saved to: {filepath}")
    else:
        print(f"❌ Error: API returned status code {response.status_code}")


if __name__ == "__main__":
    extract_crypto_data()
