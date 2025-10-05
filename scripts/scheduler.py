# scripts/scheduler.py
import schedule
import time
import subprocess

def run_pipeline():
    """Trigger the main pipeline."""
    print("⏳ Running scheduled sales data pipeline...")
    subprocess.run(["python", "pipeline.py"])

# Schedule to run every Monday at 8 AM
schedule.every().monday.at("08:00").do(run_pipeline)

print("🕒 Scheduler started. Waiting for next run...")

while True:
    schedule.run_pending()
    time.sleep(60)
