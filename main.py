import smtplib
from classified import email_password


#The email you want to use to send 
my_email = "codingneatpete@gmail.com"


#connect to email provider smtp server with this object
# For the class, .SMTP(), you must specify the location of email provider's SMTP server in the first parameter. For Gmail, it's smtp.gmail.com
connection = smtplib.SMTP("smtp.gmail.com")

#secruring the connection to our email server; messages will be encrpted when this is enabled
connection.starttls()

#logging in
connection.login(user=my_email, password=email_password)