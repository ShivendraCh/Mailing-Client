import mimetypes  # To handle file type detection
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer:
    def send_email(self, subject, body, to_email, from_email, password, attachment_path=None):
        # Create email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        if attachment_path:
            self.add_attachment(msg, attachment_path)

        # Proceed to send email via SMTP
        self.smtp_send(msg, from_email, to_email, password)

    def add_attachment(self, msg, file_path):
        """Add file attachment to the email"""
        try:
            ctype, encoding = mimetypes.guess_type(file_path)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'

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
        """Connect to SMTP and send the email"""
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(from_email, password)
            smtp.sendmail(from_email, to_email, msg.as_string())
            smtp.quit()
            print(f"Email sent successfully to {to_email}")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

