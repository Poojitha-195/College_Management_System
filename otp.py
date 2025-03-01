import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def send_otp(email):
    otp=random.randint(1000,9999)

    smtp_server = "smtp.gmail.com"
    smtp_port=587

    username="kodudhulapoojitha19@gmail.com"
    password="uxxl hsok cklp ysla"

    from_email="kodudhulapoojitha19@gmail.com"
    to_email=email
    subject="OTP Validation"
    body=f"OTP for teacher registration is {otp} \n Thank You"

    msg=MIMEMultipart()
    msg['From']=from_email
    msg['To']=to_email
    msg['Subject']=subject
    msg.attach(MIMEText(body,'plain'))

    server=smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(username,password)
    server.send_message(msg)
    server.quit()

    return(otp)
