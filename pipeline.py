# pipeline.py (example snippet)
from scripts.clean_data import clean_all_files
from scripts.merge_data import merge_cleaned_data
from scripts.generate_report import create_summary
from scripts.email_report import send_email

def run_pipeline():
    print("Starting automation...")
    clean_all_files()
    merged_file = merge_cleaned_data()
    report_path = create_summary(merged_file)
    send_email(report_path)
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
