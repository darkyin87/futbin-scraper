import json

from fetch_player import fetch_prices
from mail import EmailAPI


def process_prices():
    prices = fetch_prices()
    prices_str = json.dumps(prices, indent=4, sort_keys=True)
    mail = EmailAPI()
    mail.send_email(text=prices_str, subject='Player Prices')