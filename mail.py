# This Module is used to send and receive the emails
import smtplib

# MIME = Multipurpose Internet Mail Extensions, it is standard type for sending and receiving emails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, message, to_email, smtp_server, smtp_port, sender_email, sender_password):
    try:
        # Create a MIMEMultipart object to represent whole email, including body and header
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        # Create a MIMEText object to represent the email body
        msg.attach(MIMEText(message, 'plain'))

        # Establish a secure connection to the SMTP server
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, to_email, msg.as_string())

    # Print the successful or unsuccessful message
        print("Email sent successfully to " + to_email)
    except Exception as e:
        print(f"Email could not be sent. Error: " + str(e))
