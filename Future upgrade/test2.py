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


class WhiteMailer:

    def main_menu(self):
        """Main menu for the user to navigate through options"""
        while True:
            print("**Welcome to WhiteMailing**!")
            print("1. Mailer\n2. Guide\n3. Email Templates\n4. Email History\n5. Settings\n6. About the creator \n7.Quit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.mailer_menu()  # Send to mailer options
            elif choice == "2":
                self.show_guide()  # Placeholder for guide
            # Implement other choices similarly...
            elif choice == "6":
                self.about_creator()
            else:
                print("Invalid choice. Try again.")
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
            self.mail_template_menu()
        else:
            print("Invalid choice. Please try again.")
            self.mailer_menu()  # Restart the menu

    def dynamic_email(self):
        # Create the email message with headers
        msg = MIMEMultipart()
        msg['From'] = from_Email
        msg['To'] = target_email
        msg['Subject'] = input("Subject")
        msg['Date'] = formatdate(localtime=True)  # Add the Date header
        msg['Reply-To'] = from_Email  # Add a Reply-To header

        # Email body content
        body = input("Body:")
        # Attach the body to the message
        msg.attach(MIMEText(body, 'plain'))
        print("[*] Email body attached.")


    def mail_template_menu(self):
        print("Select Email Category:\n1. Formal\n2. Informal")
        category_choice = input("Enter your choice: ")

        if category_choice == "1":
            self.formal_menu()
        elif category_choice == "2":
            self.informal_menu()
        else:
            print("Invalid choice, please try again.")
            self.mail_template_menu()

    def get_email_details(self):
        recipient_name = input("Enter the recipient's name: ")
        body = input("Enter the body of the email: ")
        return recipient_name, body

    def formal_menu(self):
        print("Select Formal Email Type:\n1. Invitation\n2. Cancellation\n3. Apology")
        choice = input("Enter your choice: ")

        recipient_name, body = self.get_email_details()

        if choice == "1":
            email = self.templates.formal_invitation(recipient_name, body)
        elif choice == "2":
            email = self.templates.formal_cancellation(recipient_name, body)
        elif choice == "3":
            email = self.templates.formal_apology(recipient_name, body)
        else:
            print("Invalid choice.")
            return

        print("Generated Email Template:\n")

        # Create the email message with headers
        msg = MIMEMultipart()
        msg['From'] = from_Email
        msg['To'] = target_email
        msg['Subject'] = input("Subject")
        msg['Date'] = formatdate(localtime=True)  # Add the Date header
        msg['Reply-To'] = from_Email  # Add a Reply-To header

        # Email body content
        body = email
        # Attach the body to the message
        msg.attach(MIMEText(body, 'plain'))
        print("[*] Email body attached.")


    def informal_menu(self):
        print("Select Informal Email Type:\n1. Invitation\n2. Cancellation")
        choice = input("Enter your choice: ")

        recipient_name, body = self.get_email_details()

        if choice == "1":
            email = self.templates.informal_invitation(recipient_name, body)
        elif choice == "2":
            email = self.templates.informal_cancellation(recipient_name, body)
        else:
            print("Invalid choice.")
            return

        print("Generated Email Template:\n")
        # Create the email message with headers
        msg = MIMEMultipart()
        msg['From'] = from_Email
        msg['To'] = target_email
        msg['Subject'] = input("Subject")
        msg['Date'] = formatdate(localtime=True)  # Add the Date header
        msg['Reply-To'] = from_Email  # Add a Reply-To header

        # Email body content
        body = email
        # Attach the body to the message
        msg.attach(MIMEText(body, 'plain'))
        print("[*] Email body attached.")

    class EmailTemplates:
        def __init__(self):
            pass

        # Formal email templates
        def formal_invitation(self, recipient_name, body):
            return f"""Subject: Invitation to Business Meeting

    Dear {recipient_name},

    I would like to invite you to a business meeting scheduled for [date] at [location]. 
    We will be discussing [topic]. {body}

    Please let me know if this time works for you.

    Best regards,
    [Your Name]
    """

        def formal_cancellation(self, recipient_name, body):
            return f"""Subject: Meeting Cancellation Notice

    Dear {recipient_name},

    I regret to inform you that the meeting scheduled for [date] has been canceled due to unforeseen circumstances. 
    {body}

    We will reschedule the meeting and inform you of the new date soon.

    Best regards,
    [Your Name]
    """

        def formal_apology(self, recipient_name, body):
            return f"""Subject: Apology for the Inconvenience

    Dear {recipient_name},

    I sincerely apologize for the inconvenience caused by [specific issue]. {body}

    We are working hard to resolve the situation and appreciate your patience.

    Best regards,
    [Your Name]
    """

        # Add more formal templates similarly

        # Informal email templates
        def informal_invitation(self, recipient_name, body):
            return f"""Subject: Party at My Place!

    Hey {recipient_name},

    I’m throwing a party at my place on [date], and I’d love it if you could join us! {body}

    Let me know if you can make it.

    Cheers,
    [Your Name]
    """

        def informal_cancellation(self, recipient_name, body):
            return f"""Subject: Party Cancellation

    Hey {recipient_name},

    Sorry, but I have to cancel the party on [date] due to some unforeseen circumstances. {body}

    I’ll keep you updated about future plans.

    Take care,
    [Your Name]
    """

