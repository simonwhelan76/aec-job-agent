import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender, password, recipient, body):

    message = MIMEMultipart()

    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = "AEC Leadership Job Digest"

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as server:

        server.login(
            sender,
            password
        )

        server.send_message(message)