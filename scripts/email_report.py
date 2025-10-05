# scripts/email_report.py
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

load_dotenv()

def send_email(report_path):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    recipient = os.getenv("EMAIL_RECIPIENT")

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
