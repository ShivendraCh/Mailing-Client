import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

HOST = "smtp.gmail.com"
PORT = 587

to_Email = "Shivendracloud0309@gmail.com"

#importing email and password
from configparser import ConfigParser
config_path = "/home/joy/Com/config.ini"
config = ConfigParser()
config.read((config_path))

from_Email = config.get("smtp", "email")
passWord = config.get("smtp", "password")

# Create the message with headers
msg = MIMEMultipart()
msg['From'] = from_Email
msg['To'] = to_Email
msg['Subject'] = "Test Email from Shivendra"
msg['Date'] = formatdate(localtime=True)  # Add the Date header
msg['Reply-To'] = from_Email  # Add a Reply-To header

# Message body
body = """
Yo, This is Shivendra Mailing from python.
Hi,
Hope this works!

Thanks,
Adios.
"""

# Attach the body to the message
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server
    smtp = smtplib.SMTP(HOST, PORT)

    # Server identification and start TLS
    status_Code, response = smtp.ehlo()
    print(f"[*] Echoing the Server: {status_Code}{response}")

    status_Code, response = smtp.starttls()
    print(f"[*] Starting TLS Connection: {status_Code}{response}")

    # Login with email and password
    status_Code, response = smtp.login(from_Email, passWord)
    print(f"[*] Logging in: {status_Code}{response}")

    # Send the email
    smtp.sendmail(from_Email, to_Email, msg.as_string())
    print("[*] Email sent successfully!")

    # Close the SMTP connection
    smtp.quit()

except smtplib.SMTPException as e:
    print(f"Error occurred: {e}")
