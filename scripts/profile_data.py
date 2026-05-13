import pandas as pd

# -----------------------------
# Step 2: Basic Profiling
# -----------------------------
def profile_data(df: pd.DataFrame):
    print("Shape:", df.shape)
    print("\nColumn Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nDuplicate Rows:", df.duplicated().sum())
    print("\nSummary Stats:\n", df.describe(include='all'))