import os
from twilio.rest import Client


account_sid = "AC60c06b56f769a6d030463edd5f9e2809" #Your Twilio account ID
auth_token = "d6bfdd719f8f7aaa0ec98c8a2da1f815"    #Your secret API Token
 
client = Client(account_sid, auth_token)


if __name__ == '__main__':
    print("SMS sent")

    message = client.messages \
                    .create(
                         body="Test2",
                         from_='whatsapp:+14155238886',
                         to='whatsapp:+16479067569'
                         
                     )

    print(message.sid)