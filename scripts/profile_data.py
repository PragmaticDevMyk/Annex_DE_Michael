import pandas as pd

# -----------------------------
# Step 2: Basic Profiling
# -----------------------------
def profile_data(df: pd.DataFrame):
    with open("/opt/airflow/outputs/data_quality_report.md", "a") as f:
        print(f"Profiling of {df} data")
        print("*" * 20)
        print("Shape:", df.shape, file=f)
        print("\nColumn Types:\n", df.dtypes, file=f)
        print("\nMissing Values:\n", df.isnull().sum(), file=f)
        print("\nDuplicate Rows:", df.duplicated().sum(), file=f)
        print("\nSummary Stats:\n", df.describe(include='all'), file=f)