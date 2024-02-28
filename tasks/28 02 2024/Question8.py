# write a python program to handle exceptions when sending emails using Python's smtplib library.





import smtplib
from email.mime.text import MIMEText
 
def send_email(sender_email, recipient_email, subject, body):
    message = MIMEText(body)
 
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
 
    smtp_server = 'sandbox.smtp.mailtrap.io'
    smtp_port = '2525'
    smtp_user = '013dd476ae0657'
    smtp_pass = 'ba6f2d9aa68c1d'
 
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_pass)
 
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!")
 
    except smtplib.SMTPException as e:
        print("SMTP error occurred:", e)
 
    except Exception as e:
        print("Error occurred:", e)
 
    finally:
        if 'server' in locals():
            server.quit()
 
sender_email = input("Enter sender's email address: ")
recipient_email = input("Enter recipient's email address: ")
subject = input("Enter email subject: ")
body = input("Enter email body: ")
 
send_email(sender_email, recipient_email, subject, body)