import pandas as pd

def run_feature_engineering():
    credit_data = pd.read_csv("/opt/airflow/data/gold/credit_cleaned.csv")
    sales_data = pd.read_csv("/opt/airflow/data/gold/sales_cleaned.csv")

    # Age band
    # Convert to datetime consistently (force tz-naive or set a timezone)
    credit_data['date'] = pd.to_datetime(credit_data['date'], errors='coerce').dt.tz_localize(None)
    sales_data['date_of_birth'] = pd.to_datetime(sales_data['date_of_birth'], errors='coerce').dt.tz_localize(None)

    # Age calculation
    max_date = credit_data['date'].max()
    sales_data['age'] = (max_date - sales_data['date_of_birth']).dt.days // 365

    # Age band
    sales_data['age_band'] = pd.cut(
        sales_data['age'],
        bins=[18,25,35,45,55,120],
        labels=['18-25','26-35','36-45','46-55','55+']
    )


    # Payment ratio
    credit_data['payment_ratio'] = credit_data['total_paid'] / credit_data['total_due_today']

    # Arrears band
    credit_data['arrears_band'] = pd.cut(
        credit_data['days_past_due'],
        bins=[-1,0,7,30,9999],
        labels=['Up to date','PAR 7','PAR 30','High risk']
    )

     # Risk category
    def risk_logic(row):
        if row['account_status_l2'] == 'Paid Off':
            return 'Low'
        elif row['arrears'] > 0 and row['days_past_due'] > 30:
            return 'Critical'
        elif row['arrears'] > 0:
            return 'Medium'
        else:
            return 'Low'
    credit_data['risk_category'] = credit_data.apply(risk_logic, axis=1)

    credit_data.to_csv("/opt/airflow/outputs/credit_features.csv", index=False)
    sales_data.to_csv("/opt/airflow/outputs/sales_features.csv", index=False)