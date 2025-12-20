import streamlit as st
import pandas as pd
import os
import json
from glob import glob

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("📊 Cryptocurrency Dashboard")
st.write("This dashboard visualizes the latest processed cryptocurrency data.")

# -----------------------------------------------------
# 🔍 Locate latest JSON file
# -----------------------------------------------------
processed_dir = os.path.join("..", "data", "processed")
if not os.path.exists(processed_dir):
    st.error("❌ Processed data folder not found. Run the ETL pipeline first.")
    st.stop()

json_files = glob(os.path.join(processed_dir, "*.json"))

if not json_files:
    st.error("❌ No JSON files found. Convert or run pipeline first.")
    st.stop()

latest_json = max(json_files, key=os.path.getctime)

# -----------------------------------------------------
# 📥 Load JSON
# -----------------------------------------------------
with open(latest_json, "r") as f:
    data = json.load(f)

# Convert list of dicts → DataFrame
df = pd.DataFrame(data)

st.success(f"Loaded: `{os.path.basename(latest_json)}`")

# -----------------------------------------------------
# 📊 Dashboard Content
# -----------------------------------------------------
st.subheader("📄 Raw Data")
st.dataframe(df)

# Simple charts if numeric fields exist
numeric_cols = df.select_dtypes(include="number").columns

if len(numeric_cols) > 0:
    st.subheader("📈 Numeric Distributions")
    st.bar_chart(df[numeric_cols])
else:
    st.info("No numeric data available for charting.")
