

import smtplib
import os
from email.message import EmailMessage 
import ssl
'''
def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to

    user="rolexamit17@gmail.com"
    msg['from']=user
    password="dfrlqxwqfccyvrgd"

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()
    if __name__=='__main__':
         email_alert("hey","hello  world",bakaleamit28@gmail.com)
'''
def mailit():
    email_sender='rolexamit17@gmail.com'
    email_password="dfrlqxwqfccyvrgd"
    email_receiver='bakaleamit28@gmail.com'

    subject= 'Email Alert'
    body="Social distance violation "

    em=EmailMessage()
    em['form']=email_sender
    em['to']=email_receiver
    em['subject']=subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp :
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

