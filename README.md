# WhiteMailer - Automated Mailing Client

## Overview
WhiteMailer is a Python-based email client that allows users to send emails to one or more recipients at once. It’s designed to be simple and flexible, allowing you to customize the email content and add attachments like images. This tool can be useful for sending personalized emails in bulk, where each recipient is addressed by their name (extracted from their email).

## Features
- Supports sending to multiple recipients by separating emails with commas.
- Automatically personalizes the email body with the recipient's name (extracted from their email).
- Supports image attachments.
- Uses a secure TLS connection with Gmail SMTP.

## Usage
1. **Configure your email credentials**: Open the `config.ini` file and fill in your Gmail email and password under the `[smtp]` section.
2. **Run the script**: Execute the Python script in your terminal or IDE.
3. **Input the target emails**: When prompted, enter one or more email addresses separated by commas.
4. **Image Attachment**: Place an image path (can be commented out if not used). Refer to comments in the code for guidance.

## Example
Enter the target email(s) separated by commas: "example1@gmail.com, example2@yahoo.com"

The program will send a personalized email to each recipient, using the part of the email before the '@' symbol as their name (e.g., "example1" will be the recipient's name for "example1@gmail.com").

## Why I Built This
I created WhiteMailer to simplify bulk email communication, whether for projects, announcements, or newsletters. Often, personalization is key, and writing individual emails can be time-consuming. This script makes it easy to send personalized emails in bulk while maintaining flexibility and ease of use.

---

## About the Author
I am Shivendra Chauhan, a passionate Python developer who enjoys creating automation tools to simplify daily tasks. This mailing tool was designed as a project to help others easily send personalized bulk emails without needing extensive technical knowledge.

Feel free to modify the code and use it for your own needs. Happy emailing!
