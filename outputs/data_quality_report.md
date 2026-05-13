Shape: (1048575, 16)

Column Types:
 SALE_ID                             object
SALE_DATE                   datetime64[ns]
RETURNED                           float64
RETURN_DATE                 datetime64[ns]
SALE_TYPE                           object
SELLER                              object
SELLER_TYPE                         object
RETURN_POLICY_COMPLIANCE            object
CASH_PRICE                         float64
LOAN_PRICE                         float64
CLIENT_MODEL                        object
BUSINESS_MODEL                      object
LOAN_TERM                           object
PRODUCT_NAME                        object
MODEL                               object
Loan Id                             object
dtype: object

Missing Values:
 SALE_ID                     1027828
SALE_DATE                   1027828
RETURNED                    1027828
RETURN_DATE                 1046831
SALE_TYPE                   1027830
SELLER                      1027905
SELLER_TYPE                 1032799
RETURN_POLICY_COMPLIANCE    1046831
CASH_PRICE                  1027830
LOAN_PRICE                  1027830
CLIENT_MODEL                1027853
BUSINESS_MODEL              1027828
LOAN_TERM                   1027832
PRODUCT_NAME                1027830
MODEL                       1027830
Loan Id                     1027879
dtype: int64

Duplicate Rows: 1027827

Summary Stats:
                   SALE_ID  ...            Loan Id
count               20747  ...              20696
unique              20747  ...              20691
top     recg9SxxjvTdgP6NC  ...  rec1s8Oc6qhMCGKZ2
freq                    1  ...                  2
mean                  NaN  ...                NaN
min                   NaN  ...                NaN
25%                   NaN  ...                NaN
50%                   NaN  ...                NaN
75%                   NaN  ...                NaN
max                   NaN  ...                NaN
std                   NaN  ...                NaN

[11 rows x 16 columns]
Shape: (1048575, 5)

Column Types:
 _id              object
provider         object
date_of_birth    object
Loan Id          object
createdAt UTC    object
dtype: object

Missing Values:
 _id               991445
provider          991445
date_of_birth     991654
Loan Id          1035013
createdAt UTC     991445
dtype: int64

Duplicate Rows: 991444

Summary Stats:
                              _id  ...             createdAt UTC
count                      57130  ...                     57130
unique                     57130  ...                     57130
top     67c57f7b5a877e67ca1e9636  ...  2025-03-03T12:12:02.196Z
freq                           1  ...                         1

[4 rows x 5 columns]
Shape: (1048575, 3)

Column Types:
 Loan Id        object
Citizenship    object
Gender         object
dtype: object

Missing Values:
 Loan Id        1033679
Citizenship     998787
Gender          998792
dtype: int64

Duplicate Rows: 1038065

Summary Stats:
                   Loan Id Citizenship Gender
count               14896       49788  49783
unique              10497           3      5
top     recDXYKagrTFQRY6N      KENYAN   Male
freq                   35       46075  31329
Shape: (1048575, 6)

Column Types:
 Loan Id                         object
Duration                       float64
Received                       float64
Persons Received From Total    float64
Banks Received                 float64
Paybills Received Others       float64
dtype: object

Missing Values:
 Loan Id                        1036690
Duration                       1025736
Received                       1025736
Persons Received From Total    1025736
Banks Received                 1025736
Paybills Received Others       1025736
dtype: int64

Duplicate Rows: 1027254

Summary Stats:
                   Loan Id  ...  Paybills Received Others
count               11885  ...              2.283900e+04
unique              10609  ...                       NaN
top     rec7jCmNMPNWJHeDs  ...                       NaN
freq                   11  ...                       NaN
mean                  NaN  ...              9.228903e+04
std                   NaN  ...              4.583737e+05
min                   NaN  ...             -1.975599e+06
25%                   NaN  ...              4.250000e+02
50%                   NaN  ...              6.851700e+03
75%                   NaN  ...              4.749500e+04
max                   NaN  ...              2.200725e+07

[11 rows x 6 columns]
Shape: (71456, 34)

Column Types:
 LOAN_ID                             object
DATE                                object
CUSTOMER_AGE                         int64
TOTAL_PAID                           int64
TOTAL_DUE_TODAY                    float64
BALANCE                            float64
DAYS_PAST_DUE                        int64
CLOSING_BALANCE                    float64
ADVANCE                            float64
BALANCE_DUE_TO_DATE                float64
ARREARS                            float64
BALANCE_DUE_STATUS                  object
PAYMENT                              int64
EXPECTED_PAYMENT                   float64
FIRST_PAYMENT                        int64
FIRST_EXPECTED_PAYMENT               int64
ACCOUNT_STATUS_L1                   object
ACCOUNT_STATUS_L2                   object
RETURN_DATE                         object
SALE_DATE                           object
CREDIT_CHECK_DONE                   object
PAYMENT_AMOUNT                     float64
ADJUSTMENT_AMOUNT                  float64
PREPAYMENT_AMOUNT                    int64
DEPOSIT                            float64
WEEKLY_RATE                        float64
CREDIT_EXPIRY                       object
NEXT_INVOICE_DATE                   object
DISCOUNT                           float64
OVERPAYMENT_AMOUNT                 float64
MAX_PAYMENT_DATE                    object
INITIAL_PAY                          int64
TOTAL_PAID_WITH_ADJUSTMENTS_15D      int64
Unnamed: 28                        float64
dtype: object

Missing Values:
 LOAN_ID                                0
DATE                                   0
CUSTOMER_AGE                           0
TOTAL_PAID                             0
TOTAL_DUE_TODAY                       28
BALANCE                                8
DAYS_PAST_DUE                          0
CLOSING_BALANCE                        8
ADVANCE                                0
BALANCE_DUE_TO_DATE                   28
ARREARS                                0
BALANCE_DUE_STATUS                     0
PAYMENT                                0
EXPECTED_PAYMENT                       1
FIRST_PAYMENT                          0
FIRST_EXPECTED_PAYMENT                 0
ACCOUNT_STATUS_L1                      0
ACCOUNT_STATUS_L2                      0
RETURN_DATE                        64570
SALE_DATE                              0
CREDIT_CHECK_DONE                      0
PAYMENT_AMOUNT                     68293
ADJUSTMENT_AMOUNT                  68293
PREPAYMENT_AMOUNT                      0
DEPOSIT                                8
WEEKLY_RATE                            8
CREDIT_EXPIRY                          0
NEXT_INVOICE_DATE                      0
DISCOUNT                               0
OVERPAYMENT_AMOUNT                     0
MAX_PAYMENT_DATE                     749
INITIAL_PAY                            0
TOTAL_PAID_WITH_ADJUSTMENTS_15D        0
Unnamed: 28                        71456
dtype: int64

Duplicate Rows: 0

Summary Stats:
                   LOAN_ID  ... Unnamed: 28
count               71456  ...         0.0
unique              20742  ...         NaN
top     recnBZuKLsWCIm3cW  ...         NaN
freq                    5  ...         NaN
mean                  NaN  ...         NaN
std                   NaN  ...         NaN
min                   NaN  ...         NaN
25%                   NaN  ...         NaN
50%                   NaN  ...         NaN
75%                   NaN  ...         NaN
max                   NaN  ...         NaN

[11 rows x 34 columns]
Shape: (4129, 17)

Column Types:
 Submission ID                                                                                                                      object
Respondent ID                                                                                                                      object
Submitted at                                                                                                               datetime64[ns]
Loan Id                                                                                                                            object
Using a scale from 0 (not likely) to 10 (very likely), how likely are you to recommend ABC Phones to friends or family?           float64
What is the main reason for your score?                                                                                            object
What is one thing we could do to improve your experience with us?                                                                  object
Are you happy with the quality and performance of your device?                                                                     object
Are you happy with the service and support provided by ABC Phones?                                                                 object
Have you ever experienced a delay in your payment reflecting in your ABC account?                                                  object
Have you ever had difficulty getting assistance from ABC Phones customer support when needed?                                      object
(If Yes) – Please describe the challenge you faced and how we can improve your experience.                                         object
Have you experienced any battery-related issues with your MoPhones device?                                                         object
Have you used the MoPhones app (MoApp) to manage your account or make payments?                                                    object
Which communication channel do you prefer when contacting MoPhones for inquiries or support?                                       object
Have you ever had your phone lock despite making a payment on time?                                                                object
Any other Feedback?                                                                                                                object
dtype: object

Missing Values:
 Submission ID                                                                                                                 0
Respondent ID                                                                                                                 0
Submitted at                                                                                                                  0
Loan Id                                                                                                                       0
Using a scale from 0 (not likely) to 10 (very likely), how likely are you to recommend ABC Phones to friends or family?     144
What is the main reason for your score?                                                                                    2946
What is one thing we could do to improve your experience with us?                                                          2995
Are you happy with the quality and performance of your device?                                                             1502
Are you happy with the service and support provided by ABC Phones?                                                         1521
Have you ever experienced a delay in your payment reflecting in your ABC account?                                          1760
Have you ever had difficulty getting assistance from ABC Phones customer support when needed?                              1777
(If Yes) – Please describe the challenge you faced and how we can improve your experience.                                 2169
Have you experienced any battery-related issues with your MoPhones device?                                                 2048
Have you used the MoPhones app (MoApp) to manage your account or make payments?                                            2069
Which communication channel do you prefer when contacting MoPhones for inquiries or support?                               2092
Have you ever had your phone lock despite making a payment on time?                                                        2099
Any other Feedback?                                                                                                        2376
dtype: int64

Duplicate Rows: 0

Summary Stats:
        Submission ID  ... Any other Feedback?
count           4129  ...                1753
unique          4129  ...                1163
top          BzK4Q11  ...                  No
freq               1  ...                 354
mean             NaN  ...                 NaN
min              NaN  ...                 NaN
25%              NaN  ...                 NaN
50%              NaN  ...                 NaN
75%              NaN  ...                 NaN
max              NaN  ...                 NaN
std              NaN  ...                 NaN

[11 rows x 17 columns]
