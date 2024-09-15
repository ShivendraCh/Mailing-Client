import smtplib
from email import  encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP("smtp.gmail.com", 587)


server.ehlo()

with open("password.txt", "r") as f:
    password = f.read()

server.login("kaihitwari95@gmail.com", password)

msg = MIMEMultipart()
msg["From"]="Shivendra Chauhan"
msg["To"]="shivendrachauahn0309@gmail.com"
msg["Subject"]="Test message"

with open("Message.txt", "r") as f:
    message =f.read()

msg.attach(MIMEText(message, "plain"))
