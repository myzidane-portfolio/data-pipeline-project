# 🚀 Cryptocurrency Data Pipeline (JSON-Based ETL)

A complete **end-to-end data pipeline project** that extracts real-time cryptocurrency market data, transforms it into a clean analytical format, and serves it through an interactive **Streamlit dashboard**. This project is designed as a **portfolio-ready data engineering project**, demonstrating modern ETL practices using **JSON data**, Python scripting, Jupyter notebooks, and lightweight analytics visualization.

## 📌 Project Overview

This repository implements a **three-stage ETL pipeline**: **Extract** (pull live cryptocurrency data from a public API), **Transform** (clean, standardize, and structure raw JSON data), and **Load** (prepare a final analytics-ready dataset). The final output is consumed by a **Streamlit dashboard** for interactive exploration.

## 🧱 Project Structure

data-pipeline-project/  
├── data/  
│   ├── raw/          Raw JSON data (source of truth)  
│   ├── processed/    Cleaned and structured JSON  
│   └── final/        Final analytics-ready JSON  
├── notebooks/  
│   ├── 01_extract_data.ipynb  
│   ├── 02_transform_data.ipynb  
│   └── 03_load_data.ipynb  
├── scripts/  
│   ├── extract.py  
│   ├── transform.py  
│   └── load.py  
├── dashboard/  
│   ├── dashboard.py  Streamlit application  
│   └── app.py        Optional / legacy file  
├── venv/             Virtual environment  
├── requirements.txt  
└── README.md  

## 🔄 ETL Pipeline Breakdown

**Extract — Raw Data**  
Data is sourced from the **CoinGecko public API** and stored in **JSON format** without modification to preserve data integrity. Each extraction produces a **timestamped raw file** for reproducibility (e.g., `data/raw/crypto_raw_YYYYMMDD_HHMMSS.json`).

**Transform — Processed Data**  
The transformation stage parses nested API responses, extracts time-series price data, converts timestamps to readable datetime, standardizes the schema (`timestamp`, `price`), and removes invalid or missing values. The transformation logic is designed to be **robust to API structure changes**. Output files are saved as timestamped JSON (e.g., `data/processed/crypto_processed_YYYYMMDD_HHMMSS.json`).

**Load — Final Dataset**  
The load stage performs lightweight validation and sorting to produce a single analytics-ready dataset used by the dashboard. The final output is saved as `data/final/crypto_final.json`.

## 📊 Streamlit Dashboard

The Streamlit dashboard provides interactive price time-series visualization, displays the latest cryptocurrency price, and offers a clean, minimal analytics interface. To run the dashboard:  
`streamlit run dashboard/dashboard.py`  
If the dashboard loads successfully, the pipeline is fully operational.

## ⚙️ Setup Instructions

Create and activate a virtual environment, then install dependencies:  
`python -m venv venv`  
`source venv/Scripts/activate` (Windows Git Bash)  
`pip install -r requirements.txt`

## ▶️ Run the Pipeline (Scripts)

Execute the ETL pipeline in order to generate fresh JSON data:  
`python scripts/extract.py`  
`python scripts/transform.py`  
`python scripts/load.py`

## 📓 Notebook Usage

The `notebooks/` directory mirrors the pipeline logic and is intended for **exploration, debugging, documentation, and demonstration**. Recommended execution order is `01_extract_data.ipynb`, `02_transform_data.ipynb`, then `03_load_data.ipynb`. The notebooks follow the same logic as the scripts with detailed explanations.

## 🧠 Key Skills Demonstrated

API data ingestion, JSON-based ETL pipelines, data cleaning and transformation, modular Python scripting, Streamlit dashboard development, reproducible project structure, and professional documentation.

## 🚀 Future Improvements

Potential enhancements include multi-cryptocurrency support, database storage (PostgreSQL/SQLite), automated scheduling (cron/Airflow), advanced analytics (returns, volatility), and deployment (Docker/Streamlit Cloud).

## 📜 License

This project is open-source and intended for **educational and portfolio use**.

## 🙌 Author

Built as part of a **data science/data engineering portfolio** to demonstrate practical, real-world ETL and analytics workflows.
