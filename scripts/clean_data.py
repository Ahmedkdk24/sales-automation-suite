# scripts/clean_data.py
import pandas as pd
import os
from glob import glob

RAW_DIR = "data/raw"
CLEANED_DIR = "data/cleaned"

def clean_file(filepath):
    """Clean a single sales data file and return a cleaned DataFrame."""
    df = pd.read_excel(filepath) if filepath.endswith('.xlsx') else pd.read_csv(filepath)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Basic cleaning
    df.dropna(how='all', inplace=True)  # Remove empty rows
    df = df.drop_duplicates()            # Remove duplicates
    df.fillna(0, inplace=True)           # Fill missing values with 0

    # Example: Ensure numeric columns
    if 'sales' in df.columns:
        df['sales'] = pd.to_numeric(df['sales'], errors='coerce').fillna(0)

    # Add a branch/source column
    branch_name = os.path.splitext(os.path.basename(filepath))[0]
    df['branch'] = branch_name

    return df

def clean_all_files():
    """Clean all files in the raw folder and save them into cleaned folder."""
    os.makedirs(CLEANED_DIR, exist_ok=True)
    files = glob(os.path.join(RAW_DIR, '*.*'))

    for file in files:
        print(f"Cleaning {file} ...")
        df = clean_file(file)
        output_path = os.path.join(CLEANED_DIR, os.path.basename(file))
        df.to_csv(output_path, index=False)
        print(f"Saved cleaned file to {output_path}")

    print("✅ All files cleaned successfully.")

if __name__ == "__main__":
    clean_all_files()
