import os
import requests

TILL_URL = os.environ.get("TILL_URL")


class TillSmsApi():
    def __init__(self):
        self.to_phone = os.environ.get("BAK_PHONE")

    def send_text(self, text):
        response = requests.post(TILL_URL, json={
            "phone": [self.to_phone],
            "text" : text
        })
        if response.status_code == 200:
            print "SMS sent successfully to %s" % self.to_phone
        else:
            print "SMS  to %s failed with response code %s" % (self.to_phone, response.status_code)


"""
*****************************************************************
Alltel                          [10-digit phone number]@message.alltel.com
                Example: 1234567890@message.alltel.com
AT&T (formerly Cingular)        [10-digit phone number]@txt.att.net
                                [10-digit phone number]@mms.att.net (MMS)
                                [10-digit phone number]@cingularme.com
                Example: 1234567890@txt.att.net
Boost Mobile                    [10-digit phone number]@myboostmobile.com
                Example: 1234567890@myboostmobile.com
Nextel (now Sprint Nextel)  [10-digit telephone number]@messaging.nextel.com
                Example: 1234567890@messaging.nextel.com
Sprint PCS (now Sprint Nextel)  [10-digit phone number]@messaging.sprintpcs.com
                                [10-digit phone number]@pm.sprint.com (MMS)
                Example: 1234567890@messaging.sprintpcs.com
T-Mobile                    [10-digit phone number]@tmomail.net
                Example: 1234567890@tmomail.net
US Cellular                 [10-digit phone number]@email.uscc.net (SMS)
                                [10-digit phone number]@mms.uscc.net (MMS)
                Example: 1234567890@email.uscc.net
Verizon                         [10-digit phone number]@vtext.com
                                [10-digit phone number]@vzwpix.com (MMS)
                Example: 1234567890@vtext.com
Virgin Mobile USA           [10-digit phone number]@vmobl.com
                Example: 1234567890@vmobl.com
*****************************************************************
"""

import smtplib
import time
from time import gmtime, strftime, localtime


class SmptpApi():
    def __init__(self):
        self.username = os.environ.get("GMAIL_USERNAME")
        self.password = os.environ.get("GMAIL_PASSWORD")
        self.fromaddr = os.environ.get("GMAIL_USERNAME")
        self.toaddrs  = os.environ.get('BAK_PHONE_EMAIL')
        self.subject = 'prices'

    def get_full_time(self):
        return strftime("%a, %d %b %Y %H:%M:%S", localtime())

    def send_text(self, msg):
        # The actual mail send
        print "Trying to send message to %s at %s" % (self.toaddrs, self.get_full_time())
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username, self.password)
        message = ("From: %s\r\n" % self.fromaddr
                 + "To: %s\r\n" % self.toaddrs
                 + "Subject: %s\r\n" % self.subject
                 + "\r\n"
                 + msg)
        server.sendmail(self.fromaddr, self.toaddrs, message)
        server.quit()


from googlevoice import Voice
from googlevoice.util import input

class GoogleVoiceApi():
    def __init__(self):
        self.voice = Voice()
        self.username = os.environ.get("GMAIL_USERNAME")
        self.password = os.environ.get("GMAIL_PASSWORD")
        self.voice.login(self.username, self.password)
        self.to_phone = os.environ.get("BAK_PHONE")

    def get_full_time(self):
        return strftime("%a, %d %b %Y %H:%M:%S", localtime())

    def send_text(self, msg):
        print "Trying to send message to %s at %s" % (self.to_phone, self.get_full_time())
        return self.voice.send_sms(self.to_phone, msg)