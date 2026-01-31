# 🚀 Cryptocurrency Data Pipeline (JSON-Based ETL)

A complete **end-to-end data pipeline project** that extracts cryptocurrency market data from a public API, transforms raw JSON into clean analytical datasets, and serves the results through an interactive **Streamlit dashboard**.

This project is designed as a **portfolio-ready Data Engineering project**, showcasing modern ETL practices, automation with **GitHub Actions**, and a clean, reproducible project structure.

## 📌 Project Overview

This repository implements a **three-stage ETL pipeline**:

- **Extract** — Collect raw cryptocurrency data from a public API  
- **Transform** — Clean, normalize, and structure JSON data  
- **Load** — Produce analytics-ready datasets for visualization  

The pipeline is fully automated using **GitHub Actions**, and the final output is consumed by a **Streamlit dashboard** for interactive exploration.

## 🧱 Project Structure

```text
data-pipeline-project/
├── .github/workflows/
│   └── etl_pipeline.yml      Automated ETL workflow (GitHub Actions)
│
├── config/
│   └── settings.yaml         Centralized configuration
│
├── dashboard/
│   ├── dashboard.py          Streamlit dashboard logic
│   └── app.py                Streamlit entry point
│
├── data/
│   ├── raw/                  Raw JSON data (source of truth)
│   ├── processed/            Cleaned & structured data
│   └── final/                Final analytics-ready dataset
│
├── notebooks/
│   ├── 01_extract_data.ipynb Extraction exploration
│   ├── 02_transform_data.ipynb Transformation exploration
│   └── 03_load_data.ipynb    Load & validation exploration
│
├── scripts/
│   ├── extract.py            Extract layer
│   ├── transform.py          Transform layer
│   ├── load.py               Load layer
│   └── convert_to_json.py    Utility script
│
├── requirements.txt
├── README.md
└── .gitignore


---

### 🔹 BLOK 4 — ETL Pipeline Breakdown

```md
## 🔄 ETL Pipeline Breakdown

### Extract — Raw Data

Cryptocurrency market data is retrieved from a public API and stored in **raw JSON format** without modification to preserve data integrity.

Each extraction generates a **timestamped raw file** to ensure traceability and reproducibility:

crypto_raw_YYYYMMDD_HHMMSS.json


---

### Transform — Processed Data

The transformation stage:

- Parses nested API responses  
- Normalizes and standardizes the schema  
- Converts timestamps into readable datetime formats  
- Handles missing or invalid values  

The transformation logic is **robust, reusable, and modular**, producing timestamped processed datasets.

---

### Load — Final Dataset

The load stage performs lightweight validation and sorting before producing an **analytics-ready dataset**.

This dataset serves as the **single source of truth** for downstream analysis and dashboard visualization.

## 📊 Streamlit Dashboard

The Streamlit dashboard enables interactive exploration of cryptocurrency data, including:

- Time-series price visualization  
- Latest market value display  
- Clean and minimal analytical interface  

Run the dashboard locally:

```bash
streamlit run dashboard/app.py

If the dashboard loads successfully, the ETL pipeline is fully operational.


---

### 🔹 BLOK 6 — Setup Instructions

```md
## ⚙️ Setup Instructions

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt


---

### 🔹 BLOK 7 — Run Pipeline

```md
## ▶️ Run the Pipeline (Scripts)

Execute the ETL pipeline sequentially to generate fresh JSON data:

```bash
python scripts/extract.py
python scripts/transform.py
python scripts/load.py


---

### 🔹 BLOK 8 — GitHub Actions Automation

```md
## 🤖 Automation with GitHub Actions

The ETL pipeline is fully automated using **GitHub Actions**, featuring:

- Scheduled execution (every 6 hours)  
- Manual trigger via `workflow_dispatch`  
- Automated dependency installation  
- End-to-end ETL execution  
- Automatic commit of updated datasets  

Workflow configuration:

```text
.github/workflows/etl_pipeline.yml


---

### 🔹 BLOK 9 — Notebook Usage

```md
## 📓 Notebook Usage

The `notebooks/` directory mirrors the production ETL logic and is intended for:

- Exploration  
- Debugging  
- Documentation  
- Demonstration  

Recommended execution order:

1. `01_extract_data.ipynb`  
2. `02_transform_data.ipynb`  
3. `03_load_data.ipynb`

## 🧠 Key Skills Demonstrated

- API data ingestion  
- JSON-based ETL pipelines  
- Data cleaning and transformation  
- Modular Python scripting  
- CI/CD automation with GitHub Actions  
- Streamlit dashboard development  
- Reproducible and production-ready project structure  
- Professional technical documentation  

---

## 🚀 Future Improvements

Planned enhancements include:

- Multi-cryptocurrency support  
- Database integration (PostgreSQL / SQLite)  
- Advanced analytics (returns, volatility, indicators)  
- Workflow orchestration with Airflow  
- Containerization with Docker  
- Cloud deployment (Streamlit Cloud / AWS)  

---

## 📜 License

This project is open-source and intended for **educational and portfolio use**.

---

## 🙌 Author

Built as part of a **Data Engineering / Data Science portfolio** to demonstrate practical, real-world ETL automation and analytics workflows.