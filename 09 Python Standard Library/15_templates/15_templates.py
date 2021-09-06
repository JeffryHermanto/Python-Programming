# Sending Emails

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

basePath = "09 Python Standard Library/15_templates"

template = Template(Path(f"{basePath}/template.html").read_text())

message = MIMEMultipart()
message["from"] = "Jeffry Hermanto"
message["to"] = "jeffryhermanto@gmail.com"
message["subject"] = "This is a test from Python"
body = template.substitute({"name": "Jeffry"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path(f"{basePath}/jeffry.jpg").read_bytes()))

password = input("Type your password and press enter:")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("jeffryhermanto@gmail.com", password)
    smtp.send_message(message)
    print("Sent...")
