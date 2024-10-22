import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Email-sending function
def send_email(recipient_email, subject, message_body):
    try:
        sender_email = SENDER_EMAIL  # Your email from config
        app_password = EMAIL_PASSWORD  # App password from config

        # Setting up MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(message_body, 'plain'))

        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable security
        server.login(sender_email, app_password)  # Login to your email

        # Convert the message to a string and send
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        return "Email sent successfully!"

    except Exception as e:
        return f"Failed to send email. Error: {str(e)}"
