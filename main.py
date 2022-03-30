# https://myaccount.google.com/-> to enable less secure app
#pip install smtplib-> to install smtplib

import smtplib

a  = input(str("type 1 for step 1 and 2 for step 2"))

if(a=="1"):
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
elif(a=="2"):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        email1 = "pipokolo2@gmail.com"
        password = input(str("please enter the password"))

        try:
            smtp.login(email1, password)
            subject = "Money subject"
            body = "This is the body of my message"

            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(email1, 'lrichcard@gmail.com', msg)
            print("Message sent..")
        except Exception:
            print("sorry somethin went wrong")
else:print("you should have choosed 1 or 2, Bye")


