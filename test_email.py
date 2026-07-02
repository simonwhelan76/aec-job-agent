import smtplib
from email.mime.text import MIMEText

EMAIL = "swhelan.fpro@gmail.com"
APP_PASSWORD = "fgpfhxfbbpfvwzyo"

msg = MIMEText("This is a test email from the AEC Job Agent.")

msg["Subject"] = "AEC Job Agent Test"
msg["From"] = EMAIL
msg["To"] = EMAIL

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)

print("EMAIL SENT")