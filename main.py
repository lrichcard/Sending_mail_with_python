# https://myaccount.google.com/-> to enable less secure app
#pip install smtplib-> to install smtplib

import smtplib

# addin ssl
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    email1 = "pipokolo2@gmail.com"
    password = input(str("please enter the password"))

    try:
        smtp.login(email1, password)
        subject = "Money subject"
        body = "This is the body of my message\n with ssl"

        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(email1, 'lrichcard@gmail.com', msg)
        print("Message sent..")
    except Exception:
        print("sorry somethin went wrong")

