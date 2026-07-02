import smtplib
from email.mime.text import MIMEText


def send_email(sender, password, recipient, body):

    msg = MIMEText(body)

    msg["Subject"] = "AEC Leadership Job Digest"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
