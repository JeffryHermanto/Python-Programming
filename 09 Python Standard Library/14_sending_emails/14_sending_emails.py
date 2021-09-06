# Sending Emails

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

basePath = "09 Python Standard Library/14_sending_emails"

message = MIMEMultipart()
message["from"] = "Jeffry Hermanto"
message["to"] = "jeffryhermanto@gmail.com"
message["subject"] = "This is a test from Python"
message.attach(MIMEText("Body", "plain"))
message.attach(MIMEImage(Path(f"{basePath}/jeffry.jpg").read_bytes()))

password = input("Type your password and press enter:")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("jeffryhermanto@gmail.com", password)
    smtp.send_message(message)
    print("Sent...")
