import pandas as pd
import json 
import os

reports = []

os.makedirs("reports", exist_ok=True)

for i in range(1, 13):
    filename = f"file{i}.json"

    # Load JSON into DataFrame
    df = pd.read_json(filename)

    # Stats
    row_count = len(df)
    missing_per_column = df.isnull().sum().to_dict()

    report = {
        "file_name": filename,
        "row_count": row_count,
        "missing_values_per_column": missing_per_column
    }

    # Save individual report
    report_path = f"reports/report_{i}.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    reports.append({
        "file_name": filename,
        "row_count": row_count,
        "total_missing_values": sum(missing_per_column.values())
    })


df = pd.DataFrame(reports)
df.to_csv("reports/master_summary.csv", index=False)

