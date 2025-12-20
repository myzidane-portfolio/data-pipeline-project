import pandas as pd
import os

csv_file = os.path.join("data", "processed", "crypto_processed_20251123_144257.csv")
json_file = csv_file.replace(".csv", ".json")

df = pd.read_csv(csv_file)
df.to_json(json_file, orient="records", indent=4)

print("CSV → JSON conversion completed.")
print(f"Output file: {json_file}")
