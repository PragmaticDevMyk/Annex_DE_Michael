import pandas as pd
from scripts.profile_data import profile_data

def run_ingestion():
    credit_files = [
        "/opt/airflow/data/bronze/CreditData_01_01_2025.csv",
        "/opt/airflow/data/bronze/CreditData_30_03_2025.csv",
        "/opt/airflow/data/bronze/CreditData_30_06_2025.csv",
        "/opt/airflow/data/bronze/CreditData_30_09_2025.csv",
        "/opt/airflow/data/bronze/CreditData_30_12_2025.csv"
    ]

    chunks = []
    for file in credit_files:
        for chunk in pd.read_csv(file, chunksize=50000):
            chunks.append(chunk)

    credit_data = pd.concat(chunks, ignore_index=True)

    # credit_dfs = [pd.read_csv(file) for file in credit_files]
    # credit_data = pd.concat(credit_dfs, ignore_index=True)


    sales_sheets = pd.read_excel("/opt/airflow/data/bronze/SalesandCustomerData.xlsx", sheet_name=None, engine="openpyxl")
    sales_details = sales_sheets['Sales Details']
    dob_data = sales_sheets["DOB"]
    gender_data = sales_sheets["Gender"]
    income_data = sales_sheets["Income Level"]
    nps_data = pd.read_excel("/opt/airflow/data/bronze/NPS_Data.xlsx", engine="openpyxl")


    profile_data(sales_details)
    profile_data(dob_data)
    profile_data(gender_data)
    profile_data(income_data)
    profile_data(credit_data)
    profile_data(nps_data)



    credit_data.to_csv("/opt/airflow/data/silver/credit_raw.csv", index=False)
    nps_data.to_csv("/opt/airflow/data/silver/nps_raw.csv", index=False)
    sales_details.to_csv("/opt/airflow/data/silver/sales_details.csv", index=False)
    dob_data.to_csv("/opt/airflow/data/silver/dob_data.csv", index=False)
    gender_data.to_csv("/opt/airflow/data/silver/gender_data.csv", index=False)
    income_data.to_csv("/opt/airflow/data/silver/income_data.csv", index=False)