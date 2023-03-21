from twilio.rest import Client
import keys
import time

int = 1

while int == 1:
    client = Client(keys.account_sid, keys.auth_token)
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%H:%M:%S", named_tuple)

    if (time_string == "05:43:00"):
        call = client.calls.create(
            url="http://demo.twilio.com/docs/voice.xml",
            to=keys.my_phone_number,
            from_=keys.twilio_number
        )

time.sleep(1)