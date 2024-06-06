# input : receiver email address, subject line, message body 
# function : sends the email 
# References used: 
# https://docs.python.org/3/library/email.examples.html
import smtplib 

from email.message import EmailMessage

def send_email(address, subject, message):
    my_address = 'learningpython351@gmail.com'
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject 
    msg['To'] = address 
    msg['From'] = my_address 

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
    