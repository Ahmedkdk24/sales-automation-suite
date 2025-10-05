# scripts/email_report.py
import smtplib
import os
from email.message import EmailMessage

def send_email(report_path, recipient="your_email@example.com"):
    """Send the generated report via email."""
    sender = "your_email@example.com"
    password = "YOUR_APP_PASSWORD"  # Use App Password (never plain password)

    msg = EmailMessage()
    msg["Subject"] = "Weekly Sales Report"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content("Hi,\n\nPlease find attached the latest weekly sales report.\n\nRegards,\nAutomation Suite")

    with open(report_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="xlsx", filename=os.path.basename(report_path))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    send_email("data/reports/weekly_summary.xlsx")
