from twilio.rest import Client
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("my_email")
password = os.getenv("password")


#Twillo
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
from_number = os.getenv("from_number")
to_number = os.getenv("to_number")

class NotificationManager:
    def __init__(self,message):
        self.message = message
    
    def send_sms(self):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body = self.message,
            from_ = from_number,
            to = to_number,
            )
    
    def send_email(self,email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email , password=password)
            letter = "".join(self.message)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:New Low Price Flight!\n\n{letter}")
            connection.close()
