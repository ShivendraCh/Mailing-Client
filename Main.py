import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.image import MIMEImage
from configparser import ConfigParser
import os

# SMTP Server Configuration
HOST = "smtp.gmail.com"
PORT = 587

# Read email and password from the configuration file
config_path = "/home/joy/Com/config.ini"
config = ConfigParser()
config.read(config_path)

from_Email = config.get("smtp", "email")
passWord = config.get("smtp", "password")

# Welcome menu
print("Welcome to WhiteMailer:")
choice = input("Do you want to send an email to a single address or multiple addresses?\nEnter 1 for single and 2 for multiple: ")

if choice == "1":
    target_email = input("Enter the target's email: ")
    target_emails = [target_email]  # Convert to a list to handle uniformly
elif choice == "2":
    target_emails = input("Enter the target emails separated by commas: ").split(",")
    target_emails = [email.strip() for email in target_emails]  # Strip whitespace
else:
    print("[!] Invalid choice.")
    exit(1)

target_name = input("Enter the target's name: ")

# Path to the image
image_path = "/home/joy/Downloads/IMG_20240918_202529.jpg"

# Create the email message with headers
msg = MIMEMultipart()
msg['From'] = from_Email
msg['Subject'] = f"Hello {target_name}! This is your chance to be R$CH"
msg['Date'] = formatdate(localtime=True)  # Add the Date header
msg['Reply-To'] = from_Email  # Add a Reply-To header

# Email body content
body = """
Hey! Are you tired of your boring job?
Want to get rich quick?
Hi,
This is Anuradha from 21 din mein paisa double!
This is a totally legit company that will double your money in 21 days.
Our certification is called "Trust me bro".
Reply with your credit card information to apply.

Thanks,
Adios.
"""

# Attach the body to the message
msg.attach(MIMEText(body, 'plain'))
print("[*] Email body attached.")

# Open and attach the image
try:
    with open(image_path, 'rb') as img_file:
        img_data = img_file.read()
        image = MIMEImage(img_data, name=os.path.basename(image_path))
        image.add_header("Content-ID", "<image1>")
        msg.attach(image)
    print("[*] Image attached successfully.")
except FileNotFoundError:
    print(f"[!] Error: Image file not found at {image_path}.")
    exit(1)

try:
    # Connect to the SMTP server
    smtp = smtplib.SMTP(HOST, PORT)
    print(f"[*] Connecting to SMTP server {HOST} on port {PORT}...")

    # Server identification and start TLS
    status_Code, response = smtp.ehlo()
    print(f"[*] Server response after EHLO command: {status_Code} {response.decode()}")

    status_Code, response = smtp.starttls()
    print(f"[*] TLS connection started: {status_Code} {response.decode()}")

    # Login with email and password
    status_Code, response = smtp.login(from_Email, passWord)
    print(f"[*] Login status: {status_Code} {response.decode()}")

    # Send the email to each recipient
    for target_email in target_emails:
        msg['To'] = target_email
        smtp.sendmail(from_Email, target_email, msg.as_string())
        print(f"[*] Email sent successfully to {target_email}!")

    # Close the SMTP connection
    smtp.quit()
    print("[*] SMTP connection closed.")

except smtplib.SMTPException as e:
    print(f"[!] SMTP error occurred: {e}")
