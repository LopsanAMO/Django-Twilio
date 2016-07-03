from twilio.rest import TwilioRestClient
from twilio import twiml

def send_message(mensaje):
    ACCOUNT_SID = "YOUR_ACCOUNT_SID"
    AUTH_TOKEN = "YOUR_AUTH_TOKEN"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
    	to="+YOUR_PHONE",
    	from_="YOUR_TWILIO_PHONE",
    	body=mensaje,
    )
