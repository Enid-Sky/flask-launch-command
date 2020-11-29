from twilio.rest import Client
import os

send_to = os.environ['USER_NUMBER']
twilio = os.environ['TWILIO_NUMBER']
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    to=send_to,
    from_=twilio,
    body='STARLINK NOV 28 2020'
)
# reminder = request.form.get('reminder')
flash(f'A reminder has been sent.')
print(message.sid)

# account_sid = os.environ['ACCOUNT_SID']
# auth_token = os.environ['AUTH_TOKEN']

# print(account_sid)
# print(auth_token)

# client = Client(account_sid, auth_token)


# message = client.messages.create(
#     body="STARLINK NOV 28 2020",
#     to='+13108823819',
#     from_='+13158193842'
# )
# print(message.sid)
