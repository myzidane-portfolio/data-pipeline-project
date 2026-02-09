# 🚀 `Cryptocurrency Data Pipeline (JSON-Based ETL)`

A complete **end-to-end data pipeline project** that extracts real-time cryptocurrency market data, transforms it into a clean analytical format, and serves it through an interactive **Streamlit dashboard**.

This project is designed as a **portfolio-ready Data Engineering project**, demonstrating modern ETL practices using **JSON data**, Python scripting, Jupyter notebooks, GitHub Actions automation, and lightweight analytics visualization.

## 📌 `Project Overview`

This repository implements a **three-stage ETL pipeline**:

- **Extract** — Retrieve live cryptocurrency data from a public API  
- **Transform** — Clean, normalize, and standardize raw JSON data  
- **Load** — Produce a final analytics-ready dataset  

The final dataset is consumed by a **Streamlit dashboard** for interactive time-series analysis and monitoring.

## 🧱 `Project Structure`

```text
data-pipeline-project/
├── .github/workflows/
│   └── etl_pipeline.yml      Automated ETL workflow (GitHub Actions)
├── config/
│   └── settings.yaml         Centralized configuration
├── dashboard/
│   ├── dashboard.py          Streamlit dashboard logic
│   └── app.py                Streamlit entry point
├── data/
│   ├── raw/                  Raw JSON data (source of truth)
│   ├── processed/            Cleaned & structured data
│   └── final/                Final analytics-ready dataset
├── notebooks/
│   ├── 01_extract_data.ipynb
│   ├── 02_transform_data.ipynb
│   └── 03_load_data.ipynb
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── convert_to_json.py
├── requirements.txt
├── README.md
└── .gitignore

---

### 🔹 BLOK 4 — ETL Pipeline Breakdown

```markdown
## 🔄 `ETL Pipeline Breakdown`

### Extract — Raw Data
Cryptocurrency market data is retrieved from a public API and stored in **raw JSON format** without modification to preserve data integrity.  
Each extraction generates a **timestamped raw file** (e.g. `crypto_raw_YYYYMMDD_HHMMSS.json`) to ensure traceability and reproducibility.

### Transform — Processed Data
The transformation stage parses nested API responses, normalizes the schema, converts timestamps into readable datetime formats, handles missing or invalid values, and standardizes key fields such as price and volume.  
Processed outputs are saved as **timestamped JSON datasets**.

### Load — Final Dataset
The load stage performs lightweight validation and sorting before saving a **final analytics-ready dataset**, which serves as the single source of truth for downstream analysis and dashboard visualization.
