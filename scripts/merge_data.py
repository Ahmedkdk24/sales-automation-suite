# scripts/merge_data.py
import pandas as pd
import os
from glob import glob

CLEANED_DIR = "data/cleaned"
MERGED_PATH = "data/reports/merged_sales.csv"

def merge_cleaned_data():
    """Merge all cleaned CSV files into a single master file."""
    os.makedirs(os.path.dirname(MERGED_PATH), exist_ok=True)
    files = glob(os.path.join(CLEANED_DIR, '*.csv'))

    if not files:
        raise FileNotFoundError("No cleaned files found to merge.")

    dfs = [pd.read_csv(file) for file in files]
    merged_df = pd.concat(dfs, ignore_index=True)

    merged_df.to_csv(MERGED_PATH, index=False)
    print(f"✅ Merged data saved to {MERGED_PATH}")
    return MERGED_PATH

if __name__ == "__main__":
    merge_cleaned_data()
