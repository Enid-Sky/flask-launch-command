from twilio.rest import Client
import os


def reminder():
    send_to = os.environ['USER_NUMBER']
    twilio = os.environ['TWILIO_NUMBER']
    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=send_to,
        from_=twilio,
        body=f'Upcoming launch reminder.'
    )

    print(message.sid)

    return message
