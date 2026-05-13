import os
import pandas as pd
from datetime import datetime

def quality_check():

      # Paths to cleaned data
    credit_path = "/opt/airflow/data/gold/credit_cleaned.csv"
    sales_path = "/opt/airflow/data/gold/sales_cleaned.csv"
    nps_path = "/opt/airflow/data/gold/nps_cleaned.csv"

    # Load datasets
    credit_df = pd.read_csv(credit_path)
    sales_df = pd.read_csv(sales_path)

    # -------------------------------
    # 1. Freshness Check
    # -------------------------------
    mtime = os.path.getmtime(credit_path)
    last_modified = datetime.fromtimestamp(mtime)
    if (datetime.now() - last_modified).days > 1:
        raise ValueError("❌ Freshness check failed: credit_cleaned.csv is stale")



    # -------------------------------
    # 2. Null Value Check
    # -------------------------------
    if credit_df.isnull().any().any():
        print("⚠️ Warning: Null values detected in credit data")
    if sales_df.isnull().any().any():
        print("⚠️ Warning: Null values detected in sales data")

    # -------------------------------
    # 3. Schema Consistency
    # -------------------------------
    expected_credit_cols = {'loan_id','date','arrears','days_past_due'}
    expected_sales_cols = {'loan_id','date_of_birth'}

    if not expected_credit_cols.issubset(set(credit_df.columns)):
        raise ValueError("❌ Schema check failed: credit data missing expected columns")
    if not expected_sales_cols.issubset(set(sales_df.columns)):
        raise ValueError("❌ Schema check failed: sales data missing expected columns")

    print("✅ All data quality checks passed successfully")