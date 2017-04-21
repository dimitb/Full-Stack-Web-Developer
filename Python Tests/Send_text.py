"""Sends a text message using Twilio client"""


from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC11fc880508a19251642ddc33a9d6e1d2"
# Your Auth Token from twilio.com/console
auth_token  = "a6ded3b51337ea588863ed94dcd47df1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17757415730", 
    from_="+17752040754",
    body="If boys had uteruses theyd be called duderuses")

print(message.sid)
