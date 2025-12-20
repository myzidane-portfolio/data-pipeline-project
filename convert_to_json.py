import pandas as pd
import os

csv_path = "../data/processed/crypto_processed_20251123_144257.csv"
json_path = csv_path.replace(".csv", ".json")

df = pd.read_csv(csv_path)
df.to_json(json_path, orient="records", indent=4)

print(f"JSON saved to: {json_path}")
