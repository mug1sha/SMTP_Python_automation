import getpass
import smtplib

# Gmail SMTP settings
HOST = "smtp.gmail.com"
PORT = 587

FROM_EMAIL = "godsonmugisha2015@gmail.com"  # Replace with your Gmail
TO_EMAIL = "goaln23@gmail.com"

# Use app password here (or prompt securely if testing)
PASSWORD = getpass.getpass("Enter your Gmail App Password: ")

MESSAGE = """\
Subject: Mail from the scammer

Hi My Friend,
I just wanted to say hello, and tell you that I'm a scammer!
Thanks!
"""

# Setup SMTP
smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()
