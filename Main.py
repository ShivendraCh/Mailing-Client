import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.image import MIMEImage
from configparser import ConfigParser
import os

# SMTP Server Configuration (using Gmail's SMTP server)
HOST = "smtp.gmail.com"
PORT = 587

# Read email credentials (email and password) from the configuration file
config_path = "config.ini"  # Adjust the path if the config.ini is elsewhere
config = ConfigParser()
config.read(config_path)

# Fetch the user's email and password from the config file
from_Email = config.get("smtp", "email")  # Ensure your email is correctly set in config.ini
passWord = config.get("smtp", "password")  # Ensure your password is correctly set in config.ini

# Welcome message to guide users
print("Welcome to WhiteMailer!")
print("You can send an email to one or more recipient(s) by separating the email addresses with commas.")

# Input target emails from the user (multiple emails separated by commas)
target_emails = input("Enter the target email(s) separated by commas: ").split(",")
target_emails = [email.strip() for email in target_emails]  # Clean up any whitespace

# Image path for attaching an image to the email
# Example: image_path = "/path/to/your/image.jpg" or leave blank if no image is attached
image_path = "your/image/path/here.jpg"  # <--- Example: "/home/user/images/sample.jpg"

# Default email body content with a suggestion for users to customize
# Users should replace this default text with their custom message.
body_template = """
Hi {name},

This is a default email body. Please modify this text to reflect your own message before sending the email. 
For example, you might want to inform recipients about a project update, a meeting, or any other announcement.

Best regards,
[Your Name]
"""

# Try to open and read the image file
try:
    with open(image_path, 'rb') as img_file:
        img_data = img_file.read()
        print("[*] Image loaded successfully.")
except FileNotFoundError:
    print(f"[!] Error: Image file not found at {image_path}. Please check your image path or comment out this section.")
    img_data = None  # If image is not found, we skip attaching it

try:
    # Connecting to the SMTP server
    smtp = smtplib.SMTP(HOST, PORT)
    print(f"[*] Connecting to SMTP server {HOST} on port {PORT}...")

    # Server identification and start TLS (encrypted connection)
    status_Code, response = smtp.ehlo()
    print(f"[*] Server response after EHLO command: {status_Code} {response.decode()}")

    status_Code, response = smtp.starttls()
    print(f"[*] TLS connection started: {status_Code} {response.decode()}")

    # Login to the SMTP server with the provided email and password
    status_Code, response = smtp.login(from_Email, passWord)
    print(f"[*] Login status: {status_Code} {response.decode()}")

    # Loop through each provided email, extract the name before '@', and send personalized email
    for target_email in target_emails:
        if "@" in target_email:
            target_name = target_email.split("@")[0]  # Extract name before '@'
        else:
            print(f"[!] Invalid email format: {target_email}")
            continue

        # Create a new email message for each recipient
        msg = MIMEMultipart()
        msg['From'] = from_Email
        msg['To'] = target_email
        msg['Subject'] = f"Personalized Email for {target_name.capitalize()}"
        msg['Date'] = formatdate(localtime=True)
        msg['Reply-To'] = from_Email

        # Personalize the email body with the extracted name
        body = body_template.format(name=target_name.capitalize())
        msg.attach(MIMEText(body, 'plain'))
        print(f"[*] Email body prepared for {target_email}.")

        # Attach the image (if it exists)
        if img_data:
            image = MIMEImage(img_data, name=os.path.basename(image_path))
            image.add_header("Content-ID", "<image1>")
            msg.attach(image)

        # Send the email
        smtp.sendmail(from_Email, target_email, msg.as_string())
        print(f"[*] Email sent successfully to {target_email}!")

    # Close the SMTP connection
    smtp.quit()
    print("[*] SMTP connection closed.")

except smtplib.SMTPException as e:
    print(f"[!] SMTP error occurred: {e}")
