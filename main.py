import smtplib
from classified import email_password


# The email you want to use to send 
# Must turn on 2-step verification for Gmail and create an app password
my_email = "codingneatpete@gmail.com"

receiving_email = "peterhyh@yahoo.com"

my_message = "My Subject"


# Connect to email provider smtp server with this object
# For the class, .SMTP(), you must specify the location of email provider's SMTP server in the first parameter. For Gmail, it's smtp.gmail.com
with smtplib.SMTP("smtp.gmail.com") as connection:

    # Secruring the connection to our email server; messages will be encrpted when this is enabled
    connection.starttls()

    # Logging in
    connection.login(user=my_email, password=email_password)

    # Sending the mail
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=receiving_email, 
        msg=f"Subject: {my_message}\n\nThis is the body of my email."
    )


