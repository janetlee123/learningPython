# input : receiver email address, subject line, message body 
# function : sends the email 
# References used: 
# https://developers.google.com/gmail/api/quickstart/python 
# https://realpython.com/python-send-email/ 


def send_email(address, subject, message):
    
    #Exceptions
    if not (isinstance(address,str) or isinstance(subject,str) 
            or isinstance(message,str)):
        raise TypeError(f"address, subject and message must be a string ")

    #