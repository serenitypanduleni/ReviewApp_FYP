# References - https://www.twilio.com/en-us/blog/verify-phone-numbers-django-twilio-verify

# Twilio Imports 
import os
from twilio.rest import Client 
from twilio.base.exceptions import TwilioRestException

twilio_client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN")
)
verify_service = twilio_client.verify.services(os.getenv("TWILIO_VERIFY_SERVICE_SID"))

def send_verification_code(phone_number):
    verify_service.verifications.create(to=phone_number.as_e164, channel="sms")


def check_verification_code(phone_number, verification_code):
    try:
        result = verify_service.verification_checks.create(
            to=phone_number.as_e164, code=verification_code
        )
    except TwilioRestException:
        return False
    return result.status == "approved"