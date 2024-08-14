import os
import smtplib


class NotificationManager:

    def __init__(self):
        self.email = ""

    def send_msg(self):
        msg = smtplib.SMTP
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body="message_body",
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )


