from configparser import ConfigParser
import getpass
from Mailer import Mailer

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

    def sender_mail(self, email_choice):
        """Select the mail to use"""
        global from_Email, alt_mail, passWord, alt_mail_password
        if email_choice == "1":
            # Read email and password from the configuration file
            config_path = "/home/joy/Com/config.ini"
            config = ConfigParser()
            config.read(config_path)

            from_Email = config.get("smtp", "email")
            passWord = config.get("smtp", "password")
            print(f"Using default email: {from_Email}")
            # You can now proceed to use the from_Email and passWord

        elif email_choice == "2":
            # Get a new email from the user
            alt_mail = input("Enter your email of choice: ")
            alt_mail_password = getpass.getpass("Enter your password: ")
            print("Email and password entered successfully.")
            # You can now use alt_mail and alt_mail_password for sending emails

        else:
            print("Invalid choice. Please select a valid option.")

        # Proceed with email sending logic using the selected email and password
        self.send_email(from_Email if email_choice == "1" else alt_mail,
                        passWord if email_choice == "1" else alt_mail_password)
