📌 Project Overview
This project implements a complete ETL (Extract, Transform, Load) pipeline using Apache Airflow and Python. It automates the ingestion of raw datasets, applies cleaning and transformation logic, performs feature engineering, and loads the processed data into a cloud storage destination (Google Cloud Storage or S3).

The pipeline is designed for scalability, modularity, and data quality monitoring, making it suitable for production-grade analytics workflows.

⚙️ Architecture
The pipeline consists of four main stages:

Ingestion

Reads raw CSV and Excel files (multi-sheet support).

Consolidates credit, sales, and NPS datasets.

Cleaning

Standardizes column names and datatypes.

Removes duplicates and handles missing values.

Validates schema consistency.

Feature Engineering

Derives customer age bands, arrears bands, payment ratios, loan maturity progress, and risk categories.

Adds behavioral features for portfolio monitoring.

Loading

Uploads processed datasets to Google Cloud Storage (GCS) or Amazon S3.

Organizes files under partitioned prefixes (e.g., cleaned/YYYY-MM-DD/).

Data Quality Checks

Freshness: ensures files are updated daily.

Uniqueness: validates primary keys (LOAN_ID, CUSTOMER_ID).

Referential Integrity: ensures all credit records map to valid customers.

📂 Project Structure
Code
etl_pipeline/
├── dags/
│   └── abc_phones_etl_dag.py        # Airflow DAG definition
├── scripts/
│   ├── ingest.py                    # Ingestion logic
│   ├── clean.py                     # Cleaning logic
│   ├── feature_engineering.py       # Feature engineering
│   ├── load_gcs.py                  # Load to GCS
│   └── load_s3.py                   # Load to S3 (optional)
├── data/                            # Raw data files (local dev only)
└── README.md                        # Project documentation
🚀 Setup Instructions
Clone the repository

bash
git clone https://github.com/PragmaticDevMyk/Annex_DE_Michael.git
cd Annex_DE_Michael
Install dependencies

bash
pip install -r requirements.txt
Configure Airflow

Place DAGs under ~/airflow/dags/.

Ensure environment variables for cloud credentials are set:

GOOGLE_APPLICATION_CREDENTIALS for GCS

AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY for S3

Run Airflow

bash
airflow db init
airflow webserver --port 8080
airflow scheduler
Trigger the DAG

Access Airflow UI at http://localhost:8080.

Enable and trigger abc_phones_etl_pipeline.

📊 Monitoring & Alerts
Logs: Available in Airflow UI per task.

Retries: Configured per task with exponential backoff.

Alerts: Extendable via Slack/Email operators for failed data quality checks.

✅ Key Benefits
Modular design with separate scripts for each ETL stage.

Automated data quality checks for reliability.

Cloud-native storage integration (GCS/S3).

Scalable scheduling with Airflow.
