# Write a Python program that reads email details (sender, recipient, subject, and body) 
# from user input and sends the email using Mailtrap as the SMTP server.





import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Mailtrap SMTP Configuration
SMTP_SERVER = 'sandbox.smtp.mailtrap.io'
SMTP_USERNAME = '013dd476ae0657'
SMTP_PASSWORD = 'ba6f2d9aa68c1d'
SMTP_PORT = '2525'

def send_email(sender, recipient, subject, body):
    try:
        # Create a MIMEText object to represent the email body
        email_body = MIMEText(body)

        # Create a MIMEMultipart object to represent the email
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = subject

        # Attach the email body to the MIMEMultipart object
        message.attach(email_body)

        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        # Login to the SMTP server
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # Send the email
        server.sendmail(sender, recipient, message.as_string())

        # Close the connection to the SMTP server
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    sender = input("Enter sender email address: ")
    recipient = input("Enter recipient email address: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    send_email(sender, recipient, subject, body)
