from email.message import EmailMessage
import os
import smtplib

# 1. Setup credentials and message
def send_email(email,message):
    msg = EmailMessage()
    msg["Subject"] = "New portfolio contact"
    msg["From"] = os.getenv("MY_EMAIL")
    msg["Reply-To"] = email
    msg["To"] = os.getenv("MY_EMAIL")
    msg.set_content(message)

    # 2. Connect and send
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade to secure
            server.login(os.getenv("MY_EMAIL"),os.getenv("SITE_PASSWORD") )
            server.send_message(msg)
        print("Email sent!")
    except Exception as e:
        print(f"Error: {e}")
