# 🚀 Cryptocurrency Data Pipeline (JSON-Based ETL)

A complete **end-to-end cryptocurrency data pipeline** that extracts market data from a public API, transforms raw JSON into a clean analytical format, and delivers insights through an interactive **Streamlit dashboard**. This project is designed as a **portfolio-ready data engineering project**, demonstrating modern ETL practices using **JSON-based data processing**, Python scripting, Jupyter notebooks, and **CI/CD automation with GitHub Actions**.

---

## 📌 Project Overview

This repository implements a **three-stage ETL pipeline**: **Extract**, **Transform**, and **Load**.  
The pipeline automatically pulls cryptocurrency market data, cleans and standardizes the dataset, and prepares it for analytics and visualization. The final output is consumed by a **Streamlit dashboard** for interactive exploration and monitoring.

The project follows **data engineering best practices**, including modular code structure, reproducibility, automated workflows, and version-controlled data outputs.

---

## 🧱 Project Structure

```text
data-pipeline-project/
├── .github/workflows/
│   └── etl_pipeline.yml        Automated ETL workflow (GitHub Actions)
│
├── config/
│   └── settings.yaml           Centralized configuration
│
├── dashboard/
│   ├── dashboard.py            Streamlit dashboard logic
│   └── app.py                  Streamlit entry point
│
├── data/
│   ├── raw/                    Raw JSON data (source of truth)
│   ├── processed/              Cleaned & structured data
│   ├── final/                  Final analytics-ready dataset
│   └── .gitkeep
│
├── notebooks/
│   ├── 01_extract_data.ipynb   Extraction exploration
│   ├── 02_transform_data.ipynb Transformation exploration
│   └── 03_load_data.ipynb      Load & validation exploration
│
├── scripts/
│   ├── extract.py              Extract layer
│   ├── transform.py            Transform layer
│   ├── load.py                 Load layer
│   └── convert_to_json.py
│
├── requirements.txt
├── README.md
└── .gitignore

## 🔄 ETL Pipeline Breakdown

### **Extract — Raw Data**

Cryptocurrency market data is retrieved from a **public API** and stored in **raw JSON format** without modification to preserve data integrity.  
Each extraction generates a **timestamped raw file** (e.g. `crypto_raw_YYYYMMDD_HHMMSS.json`) to ensure traceability and reproducibility.

---

### **Transform — Processed Data**

The transformation stage parses nested API responses, normalizes the schema, converts timestamps into readable datetime formats, handles missing or invalid values, and standardizes fields such as **price** and **volume**.  
The transformation logic is designed to be **robust and reusable**, producing timestamped processed datasets.

---

### **Load — Final Dataset**

The load stage performs lightweight validation and sorting before saving a **final analytics-ready dataset**.  
This dataset serves as the **single source of truth** for downstream analysis and dashboard visualization.

---

## 📊 Streamlit Dashboard

The Streamlit dashboard enables **interactive exploration** of cryptocurrency price data, including:

- Time-series price visualization  
- Latest market value display  
- Clean and minimal analytical interface  

### Run the dashboard locally:
```bash
streamlit run dashboard/app.py

If the dashboard loads successfully, the ETL pipeline is fully operational.

## ⚙️ Setup Instructions

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt

## ▶️ Run the Pipeline (Scripts)

Execute the ETL pipeline sequentially to generate fresh JSON data:

python scripts/extract.py
python scripts/transform.py
python scripts/load.py

## 🤖 Automation with GitHub Actions

The ETL pipeline is fully automated using **GitHub Actions**.

- Scheduled execution (every **6 hours**)
- Manual trigger via `workflow_dispatch`
- Automated dependency installation
- End-to-end ETL execution
- Automatic commit of updated datasets

Workflow configuration:
```text
.github/workflows/etl_pipeline.yml

## 📓 Notebook Usage

The `notebooks/` directory mirrors the production ETL logic and is intended for **exploration, debugging, documentation, and demonstration**.

Recommended execution order:
1. `01_extract_data.ipynb`
2. `02_transform_data.ipynb`
3. `03_load_data.ipynb`

---

## 🧠 Key Skills Demonstrated

- API data ingestion
- JSON-based ETL pipelines
- Data cleaning and transformation
- Modular Python scripting
- CI/CD automation with GitHub Actions
- Streamlit dashboard development
- Reproducible and production-ready project structure
- Professional technical documentation

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
