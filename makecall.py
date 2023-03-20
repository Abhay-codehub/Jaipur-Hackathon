from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

call = client.calls.create(
    url="http://demo.twilio.com/docs/voice.xml",
    to=keys.my_phone_number,
    from_=keys.twilio_number
)
