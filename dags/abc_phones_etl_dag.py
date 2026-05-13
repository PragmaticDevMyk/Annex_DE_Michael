from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Import scripts
from scripts.ingest import run_ingestion
from scripts.clean import run_cleaning
from scripts.feature_engineering import run_feature_engineering
from scripts.load import run_load
from scripts.quality_check import quality_check


default_args = {
    'owner': 'data_engineer',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='abc_phones_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    
    ingest = PythonOperator(
        task_id='ingest_data',
        python_callable=run_ingestion
    )

    clean = PythonOperator(
        task_id='clean_data',
        python_callable=run_cleaning
    )

    quality = PythonOperator(
        task_id = 'quality_check',
        python_callable = quality_check
    )

    features = PythonOperator(
        task_id='feature_engineering',
        python_callable=run_feature_engineering
    )

    load = PythonOperator(
        task_id='load_to_gcs',
        python_callable=run_load
    )


    
    # TASK DEPENDENCY
    ingest >> clean >> quality >> features >> load