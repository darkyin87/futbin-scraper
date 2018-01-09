import requests
import json

domain = 'https://www.futbin.com'
version = 18
page = 'playerPrices'

player_ids = {
  'Arturo Vidal': 181872,
  'Pierre-Emerick Aubameyang': 188567,
  'Robert Lewandowski': 188545,
  'Jerome Boateng': 183907,
  'Sergio Ramos': 155862,
  'Antoine Griezmann': 194765,
}

def fetch_prices():
  ret_val = {}
  for name, id in player_ids.iteritems():
    url = "%s/%s/%s?player=%s" % (domain, version, page, id)
    response = requests.get(url)
    data = response.json()
    ret_val[name] = data[str(id)]['prices']['ps']['LCPrice']
  return ret_val


#if __name__ == "__main__":
#  prices = fetch_prices()

