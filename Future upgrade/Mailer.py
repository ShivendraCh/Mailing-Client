# Mailer.py
import mimetypes  # To handle file type detection
import os
import smtplib
from configparser import ConfigParser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer:
    def __init__(self):
        """Initialize the Mailer class and read configuration settings."""
        self.config = ConfigParser()  # Create an instance of ConfigParser
        config_path = "/home/joy/Com/config.ini"  # Path to the configuration file
        self.config.read(config_path)  # Read the config file

    def mailer_menu(self):
        """Display the mailer menu and handle user input."""
        print("Welcome to Mailer!")
        print("Please choose between sending a dynamic email or a sample email from the mail library.")
        print("Choose 1 for dynamic mail or 2 for a sample mail")

        mailer_menu_input = input("Enter your choice: ")

        if mailer_menu_input == "1":
            self.dynamic_email()
        elif mailer_menu_input == "2":
            self.sample_email()
        else:
            print("Invalid choice. Please try again.")
            self.mailer_menu()  # Restart the menu

    def dynamic_email(self):
        """Handle sending a dynamic email with user inputs."""
        to_email = input("Enter recipient's email: ")
        subject = input("Enter subject: ")
        body = input("Enter email body: ")

        # Read email and password from the configuration file
        from_email = self.config.get("smtp", "email")
        password = self.config.get("smtp", "password")

        attachment_path = input("Enter file path for attachment (or leave blank if none): ")
        if not attachment_path.strip():  # If no attachment, set to None
            attachment_path = None

        self.send_email(subject, body, to_email, from_email, password, attachment_path)

    def sample_email(self):
        """Send a sample email with predefined content."""
        to_email = input("Enter recipient's email: ")
        subject = "Sample Email"
        body = "This is a sample email sent from the Mailer class."

        from_email = self.config.get("smtp", "email")  # Use configured email
        password = self.config.get("smtp", "password")  # Use configured password

        self.send_email(subject, body, to_email, from_email, password)

    def send_email(self, subject, body, to_email, from_email, password, attachment_path=None):
        """Create and send the email."""
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if attachment_path:
            self.add_attachment(msg, attachment_path)

        # Send the email via SMTP
        self.smtp_send(msg, from_email, to_email, password)

    def add_attachment(self, msg, file_path):
        """Add a file attachment to the email."""
        try:
            ctype, encoding = mimetypes.guess_type(file_path)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'  # Default type if not recognized

            maintype, subtype = ctype.split('/', 1)
            with open(file_path, 'rb') as file:
                part = MIMEBase(maintype, subtype)
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
                msg.attach(part)
            print("File attached successfully.")
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")

    def smtp_send(self, msg, from_email, to_email, password):
        """Connect to the SMTP server and send the email."""
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()  # Upgrade to a secure connection
            smtp.login(from_email, password)  # Login using the sender's credentials
            smtp.sendmail(from_email, to_email, msg.as_string())  # Send the email
            smtp.quit()  # Close the connection
            print(f"Email sent successfully to {to_email}")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")


# Example of how to use the Mailer class
if __name__ == "__main__":
    mailer = Mailer()
    mailer.mailer_menu()  # Start the mailer menu
