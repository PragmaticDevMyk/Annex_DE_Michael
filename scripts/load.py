import pandas as pd
from google.cloud import storage
from io import StringIO

def run_load():
    # Read processed files
    credit_data = pd.read_csv("/opt/airflow/outputs/credit_features.csv")
    sales_data = pd.read_csv("/opt/airflow/outputs/sales_features.csv")
    nps_data = pd.read_csv("/opt/airflow/gold/nps_cleaned.csv")

    # Initialize GCS client (ensure GOOGLE_APPLICATION_CREDENTIALS is set in Airflow environment)
    client = storage.Client()
    bucket_name = "abc-phones-data-pipeline"
    bucket = client.bucket(bucket_name)

    # Helper function to upload DataFrame as CSV
    def upload_df_to_gcs(df, blob_name):
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(csv_buffer.getvalue(), content_type="text/csv")

    # Upload each dataset
    upload_df_to_gcs(credit_data, "cleaned/credit_features.csv")
    upload_df_to_gcs(sales_data, "cleaned/sales_features.csv")
    upload_df_to_gcs(nps_data, "cleaned/nps_cleaned.csv")