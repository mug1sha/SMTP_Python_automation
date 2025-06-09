import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = "smtp.gmail.com"
PORT = 587

FROM_EMAIL = "godsonmugisha2015@gmail.com"  # Replace with your Gmail
TO_EMAIL = "goaln23@gmail.com"
PASSWORD = getpass.getpass("Enter your password: ")

MESSAGE = MIMEMultipart("alternative")
MESSAGE['subject'] = "Mail from a hacker"
MESSAGE['from'] = FROM_EMAIL
MESSAGE['To'] = TO_EMAIL
MESSAGE['Cc'] = FROM_EMAIL
MESSAGE['Bcc'] = FROM_EMAIL

html = "" 
with open ("mail.html", "r") as file:
    html = file.read()

html_part = MIMEText(html, 'html')
MESSAGE.attach(html_part)

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE.as_string())
smtp.quit()

