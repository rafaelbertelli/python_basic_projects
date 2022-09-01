import smtplib
import ssl
from email.message import EmailMessage

from dotenv import dotenv_values


env = dotenv_values('.env')

email_sender = env["EMAIL_SENDER"]
email_psw = env["EMAIL_PASSWORD"]

with open("src/email_composer/email_subject.txt", "r") as file:
    email_subject = file.read()

with open("src/email_composer/email_message.txt", "r") as file:
    email_message = file.read()

with open("src/email_composer/email_recipients.txt", "r") as file:
    email_recipients = file.read()

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_recipients
email['Subject'] = email_subject
email.set_content(email_message)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_psw)
    smtp.sendmail(email_sender, email_recipients, email.as_string())
