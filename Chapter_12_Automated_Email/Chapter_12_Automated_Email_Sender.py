# not tested smtp cred require
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def setup_server(smtp_server, smtp_port, email, password):
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email, password)
    return server

def create_email(sender_email, receiver_email, subject, body):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))
    return message

def attach_file(message, filename):
    attachment = open(filename, "rb")
    mime_base = MIMEBase('application', 'octet-stream')
    mime_base.set_payload((attachment).read())
    encoders.encode_base64(mime_base)
    mime_base.add_header('Content-Disposition', f"attachment; filename= {filename}")
    message.attach(mime_base)

def send_email(server, message, receiver_email):
    text = message.as_string()
    server.sendmail(message['From'], receiver_email, text)

# Example usage:
smtp_server = 'smtp.example.com'
smtp_port = 587
email = 'your_email@example.com'
password = 'your_password'
receiver_email = 'receiver_email@example.com'
subject = 'Test Email'
body = 'This is a test email with an attachment.'

server = setup_server(smtp_server, smtp_port, email, password)
message = create_email(email, receiver_email, subject, body)
attach_file(message, 'your_file.txt')
send_email(server, message, receiver_email)
server.quit()