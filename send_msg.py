from twilio.rest import Client
import keys
import time

int = 1


while int == 1:
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%H:%M:%S", named_tuple)
    client = Client(keys.account_sid, keys.auth_token)

    # time_string1 = time.strftime()

    if (time_string == "05:45:00"):
        message = client.messages.create(
            body="You will win the hackathon",
            from_=keys.twilio_number,
            to=keys.my_phone_number
        )

time.sleep(1)


