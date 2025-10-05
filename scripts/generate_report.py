# scripts/generate_report.py
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import date

REPORTS_DIR = "data/reports"

def create_summary(merged_path):
    """Generate summary metrics and charts from merged data."""
    df = pd.read_csv(merged_path)

    # Summary KPIs
    total_sales = df['sales'].sum()
    top_branch = df.groupby('branch')['sales'].sum().idxmax()
    top_product = df.groupby('product')['sales'].sum().idxmax() if 'product' in df.columns else 'N/A'

    summary = {
        "Total Sales": [total_sales],
        "Top Branch": [top_branch],
        "Top Product": [top_product],
        "Report Date": [date.today()]
    }

    summary_df = pd.DataFrame(summary)
    os.makedirs(REPORTS_DIR, exist_ok=True)
    summary_path = os.path.join(REPORTS_DIR, f"weekly_summary_{date.today()}.xlsx")
    summary_df.to_excel(summary_path, index=False)

    # Optional chart
    plt.figure(figsize=(8, 5))
    df.groupby('branch')['sales'].sum().plot(kind='bar', title='Sales by Branch')
    plt.ylabel('Total Sales')
    plt.tight_layout()
    chart_path = os.path.join(REPORTS_DIR, f"sales_chart_{date.today()}.png")
    plt.savefig(chart_path)
    plt.close()

    print(f"✅ Report and chart saved in {REPORTS_DIR}")
    return summary_path

if __name__ == "__main__":
    create_summary("data/reports/merged_sales.csv")
