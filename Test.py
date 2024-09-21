# main.py

from WhiteMailer import WhiteMailer
from Mailer import Mailer
from Configuration import Configuration

class MainApp:
    def __init__(self):
        # Initialize the WhiteMailer, Mailer, and Configuration classes
        self.white_mailer = WhiteMailer()
        self.mailer = Mailer()
        self.config = Configuration()


    def run(self):
        """Main entry point to run the application"""
        while True:
            self.white_mailer.main_menu()  # Display the main menu

            choice = input("Enter your choice: ")

            if choice == "1":
                # Enter the mailer module
                self.mailer.mailer_menu()

            elif choice == "2":
                # Guide - Implement guide logic later
                print("Guide is under construction!")

            elif choice == "3":
                # Email Templates - Load and use templates
                template_name = input("Enter the template name: ")
                template_content = self.templates.load_template(template_name)
                print(f"Loaded template: {template_content}")

            elif choice == "4":
                # Email History - Log or display email history
                print("Email History")
                self.history.display_history()

            elif choice == "5":
                # Enter the configuration module
                self.config.smtp_server_configuration()

            elif choice == "6":
                # About the creator
                print("This app was created by Shivendra Chauhan!")

            else:
                print("Invalid choice, please try again.")



