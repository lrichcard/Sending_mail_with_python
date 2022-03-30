# https://myaccount.google.com/-> to enable less secure app
#pip install smtplib-> to install smtplib

import smtplib
from email.message import EmailMessage
email1 = "pipokolo2@gmail.com"
msg = EmailMessage()
msg['Subject'] = "Money subject"
msg['From'] =  email1
msg['To'] = 'lrichcard@gmail.com'
msg.set_content('This is the body of my message\n with ssl')
password = input(str("please enter the password"))


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    try:
        smtp.login(email1, password)
        print("Message sent..")
    except Exception:
        print("sorry somethin went wrong")

