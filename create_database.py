import sqlite3
import pandas as pd

conn = sqlite3.connect("mutual_funds.db")

files = {
    "scheme_performance": "07_scheme_performance.csv",
    "monthly_sip": "04_monthly_sip_inflows.csv",
    "category_inflows": "05_category_inflows.csv",
    "industry_folio_count": "06_industry_folio_count.csv"
}

for table, csv_file in files.items():
    df = pd.read_csv(csv_file)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"{table} imported successfully!")

conn.close()
print("Database Created Successfully!")