import pandas as pd

df = pd.read_csv("04_monthly_sip_inflows.csv")
print("SIP FILE COLUMNS:")
print(df.columns)

print()

df2 = pd.read_csv("05_category_inflows.csv")
print("CATEGORY FILE COLUMNS:")
print(df2.columns)
