# 📧 Gmail SMTP Email Sender with HTML Support

This Python script allows you to send **HTML-formatted emails** using **Gmail’s SMTP server**. It supports secure login with **TLS encryption**, **App Passwords**, and uses MIME multipart messages for rich content.

---

## 🚀 Features

- ✅ Connects securely to Gmail via TLS
- ✅ Uses App Password for authentication (Gmail 2FA-compatible)
- ✅ Sends rich HTML emails
- ✅ Supports Cc and Bcc headers
- ✅ Clean error handling and debug output

---

## 📂 Project Structure

📁 SMTP/
├── mail.html # HTML email template
├── html_mail.py # for html content mail
└── README.md # This file
|__ text_mail.py # for only text mails


---

## 🔐 Gmail Setup (One-Time)

> Gmail blocks less secure apps by default. You **must enable 2FA** and use an **App Password**.

### 🛠️ Steps:
1. Go to [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Go to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
4. Create an **App Password** (Select “Mail” > “Other” > "Python SMTP")

---

## 🧪 How to Run

### 1. Clone the Repository

git clone https://github.com/your-username/smtp-email-sender.git
cd SMTP

2. Create an mail.html file (or use the sample provided)

<!-- mail.html -->
<html>
  <body>
    <h1>Hello there!</h1>
    <p>This is a test email sent using <strong>Python + Gmail SMTP</strong>.</p>
  </body>
</html>

3. Run the script

python html_email.py

You’ll be prompted to enter your App Password securely.

🛡️ Security Notes
Never hardcode passwords — use getpass or environment variables.

Don’t commit your mail.html with sensitive content unless it’s just a template.

This script is for educational and ethical use only.

✍️ Author
Godson Mug1sha (aka KING👑)
Cybersecurity Student | Python Dev | Email Hacker (ethical)
🌐 Kigali, Rwanda

🧠 Future Improvements
 Add attachments support

 Support for inline images

 Switch to OAuth2 (no App Passwords)

 GUI version with Tkinter or Electron

