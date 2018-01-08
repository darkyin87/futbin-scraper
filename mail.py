# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *


class EmailAPI():
    def __init__(self):
        self.sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        self.from_email = Email(os.environ.get('BAK_EMAIL'))

    def send_email(self, to_email=os.environ.get('BAK_EMAIL'), subject="Test Email", text="test message"):
        to_email = Email(to_email)
        content = Content("text/plain", text)
        mail = Mail(self.from_email, subject, to_email, content)
        response = self.sg.client.mail.send.post(request_body=mail.get())
        print ("Sending email to %s" % to_email)
        print(response.status_code)
        print(response.body)
        print(response.headers)