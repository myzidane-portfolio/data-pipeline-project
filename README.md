# Crypto ETL Pipeline

This repository contains a simple **ETL (Extract, Transform, Load) pipeline** for cryptocurrency data built with **Python** and automated using **GitHub Actions**.

The pipeline is designed to:

* Fetch cryptocurrency data from an external API
* Clean and transform raw data
* Store processed results in a local `data/` folder
* Run automatically on a schedule or manually on demand

---

## 📂 Repository Structure

```text
data-pipeline-project/
├── .github/
│   └── workflows/
│       └── etl_pipeline.yml      # GitHub Actions workflow
├── config/
│   └── config.py                 # Configuration (API, parameters, etc.)
├── data/                          # ETL output (generated files)
├── scripts/
│   ├── extract.py                # Extract data from API
│   ├── transform.py              # Data cleaning & transformation
│   └── load.py                   # Load / save processed data
├── venv/                          # Virtual environment (not committed)
├── .gitignore
├── README.md
└── requirements.txt (optional)
```

---

## ⚙️ Pipeline Overview

1. **Extract**
   Retrieves cryptocurrency data (e.g. price, volume, market cap) from an API.

2. **Transform**
   Cleans the data, normalizes formats, and prepares the final dataset.

3. **Load**
   Saves the transformed data into the `data/` directory (CSV / JSON).

The pipeline can be executed:

* Automatically every **6 hours** (cron schedule)
* Manually via **GitHub Actions → Run workflow**

---

## 🤖 GitHub Actions Workflow

The main workflow file is located at:

```
.github/workflows/etl_pipeline.yml
```

### Triggers

```yaml
on:
  schedule:
    - cron: "0 */6 * * *"   # every 6 hours
  workflow_dispatch:
```

---

## 🔁 Auto Commit (ON / OFF Toggle)

This pipeline supports **optional automatic commits** of ETL results, which can be **enabled or disabled using a single toggle**.

### Configuration

In the workflow file:

```yaml
env:
  ENABLE_AUTO_COMMIT: "false"
```

| Value     | Behavior                                     |
| --------- | -------------------------------------------- |
| `"false"` | ❌ No automatic commit (default, recommended) |
| `"true"`  | ✅ Automatically commits the `data/` folder   |

### Why is it disabled by default?

* Scheduled ETL jobs often **produce no new data**
* Prevents unnecessary GitHub Actions failures
* Avoids excessive automated commits

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/<username>/<repo-name>.git
cd data-pipeline-project
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\\Scripts\\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

(Or install manually: `pandas`, `requests`, `matplotlib`)

### 4. Run the ETL pipeline

```bash
python scripts/extract.py
python scripts/transform.py
python scripts/load.py
```

Processed output will be generated in the `data/` directory.

---

## 🧹 Git & Repository Rules

### Ignored by Git

* `venv/`
* `__pycache__/`
* Temporary and OS-specific files

### Not recommended to commit

* Large ETL output files (CSV / JSON)
* Credentials or API keys

---

## 🗑️ Cleaning Up Workflow Runs

If workflow runs accumulate, they can be removed using **GitHub CLI**:

```bash
gh run list
gh run delete <RUN_ID>
```

Bulk delete example (Git Bash):

```bash
for id in $(gh run list --limit 1000 --json databaseId --jq '.[].databaseId'); do
  gh run delete $id
done
```

---

## 📌 Important Notes

* Deleted workflow runs **cannot be restored**
* Auto-commit should be enabled only when necessary
* For production use, consider storing data in:

  * Cloud storage (S3 / GCS)
  * A database
  * GitHub Actions Artifacts

---

## ✨ Future Improvements

* Upload ETL results as **artifacts**
* Persist data to a database
* Add logging & monitoring
* Notifications (Slack / Email)

---

## 📄 License

This project is intended for learning and development purposes.

---

🚀 **Happy data engineering!**

