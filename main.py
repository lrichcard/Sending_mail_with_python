# https://myaccount.google.com/-> to enable less secure app
#pip install smtplib-> to install smtplib

import smtplib

# read a file
fp = open('sample.txt')
message = fp.read()
print(fp.read())
fp.close()

# sender and receiver message
email_sender = "pipokolo2@gmail.com"
email_receiver = "lrichcard@gmail.com"
password = input(str("please insert the password"))

# message = "Hello rich it is a test"

# sending settup
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_sender, password)
print("Login success")
server.sendmail(email_sender,email_receiver,message)
print("Email has benn sent to", email_receiver)