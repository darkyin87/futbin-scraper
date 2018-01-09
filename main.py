import json

from fetch_player import fetch_prices
from mail import EmailAPI
from sms import GoogleVoiceApi


def process_prices():
    prices = fetch_prices()
    prices_str = json.dumps(prices, indent=4, sort_keys=True)
    print prices_str
    mail = EmailAPI()
    mail.send_email(text=prices_str, subject='Player Prices')
    sms = GoogleVoiceApi()
    sms.send_text(prices_str)