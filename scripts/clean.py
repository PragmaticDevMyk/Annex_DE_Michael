import pandas as pd
import gc
from scripts.config import SCHEMA


def clean_columns(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

def run_cleaning():
    credit_data = pd.read_csv("/opt/airflow/data/silver/credit_raw.csv", low_memory=False, dtype=SCHEMA)
    credit_data = clean_columns(credit_data)
    nps_data = pd.read_csv("/opt/airflow/data/silver/nps_raw.csv", low_memory=False, dtype=SCHEMA)
    nps_data = clean_columns(nps_data)

    credit_data['date'] = pd.to_datetime(credit_data['date'], errors='coerce')

    credit_data = credit_data.drop_duplicates(subset=['loan_id'])


    credit_data.to_csv("/opt/airflow/data/gold/credit_cleaned.csv", index=False)
    del credit_data
    nps_data.to_csv("/opt/airflow/data/gold/nps_cleaned.csv", index=False)
    del nps_data

    sales_details = pd.read_csv("/opt/airflow/data/silver/sales_details.csv", low_memory=False, dtype=SCHEMA)
    dob_data = pd.read_csv("/opt/airflow/data/silver/dob_data.csv", low_memory=False, dtype=SCHEMA)
    gender_data = pd.read_csv("/opt/airflow/data/silver/gender_data.csv", low_memory=False, dtype=SCHEMA)
    income_data = pd.read_csv("/opt/airflow/data/silver/income_data.csv", low_memory=False, dtype=SCHEMA)

    sales_details = clean_columns(sales_details)
    dob_data = clean_columns(dob_data)
    gender_data = clean_columns(gender_data)
    income_data = clean_columns(income_data)

    # Standardize Dates
    dob_data['date_of_birth'] = pd.to_datetime(dob_data['date_of_birth'], errors='coerce', utc=True)
    sales_details['sale_date'] = pd.to_datetime(sales_details['sale_date'], errors='coerce', utc=True)

    # Deduplicate
    sales_details = sales_details.drop_duplicates(subset=['sale_id'])
    dob_data = dob_data.drop_duplicates(subset=["loan_id"])
    gender_data = gender_data.drop_duplicates(subset=["loan_id"])
    income_data = income_data.drop_duplicates(subset=["loan_id"])

    sales_details = sales_details.astype({"loan_id": "string"})
    dob_data = dob_data.astype({"loan_id": "string"})
    gender_data = gender_data.astype({"loan_id": "string"})
    income_data = income_data.astype({"loan_id": "string"})

    

    # Merge the data
 
    sales_data = sales_details.merge(
        dob_data,
        on="loan_id",
        how="left"
    )

    del sales_details, dob_data
    gc.collect()

    sales_data = sales_data.merge(
        gender_data,
        on="loan_id",
        how="left"
    )

    del gender_data
    gc.collect()

    sales_data = sales_data.merge(
        income_data,
        on="loan_id",
        how="left"
    )

    del income_data
    gc.collect()
                                
  

    sales_data.to_csv("/opt/airflow/data/gold/sales_cleaned.csv", index=False)

