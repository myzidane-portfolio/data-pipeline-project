import streamlit as st
import pandas as pd
import os
import glob

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("📊 Cryptocurrency Dashboard")
st.write("This dashboard visualizes the latest processed cryptocurrency data (JSON format).")

# ---- Locate processed JSON files ----
processed_path = "../data/processed/*.json"
files = glob.glob(processed_path)

if not files:
    st.error("❌ No processed JSON files found. Run the ETL pipeline first.")
    st.stop()

# Use the newest JSON file
latest_file = max(files, key=os.path.getmtime)

st.success(f"Loaded: **{os.path.basename(latest_file)}**")

# ---- Load JSON ----
df = pd.read_json(latest_file)

st.subheader("📄 Preview of Processed Data")
st.dataframe(df)

# ---- Charts ----
st.subheader("📈 Price Chart")
if "price" in df.columns and "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    st.line_chart(df.set_index("timestamp")["price"])
else:
    st.warning("Price data or timestamp not found in JSON.")

st.subheader("📉 Daily Returns")
if "returns" in df.columns:
    st.line_chart(df["returns"])
else:
    st.warning("Returns column not found in JSON.")
