from twilio.rest import Client

def send_sms(to, from_, body):
    account_sid = "AC1234567890abcdef1234567890abcdef"
    auth_token = "sk-1234567890abcdef1234567890abcdef"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body,
        from_=from_,
        to=to
    )
    return message.sid
