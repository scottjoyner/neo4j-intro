from requests import Request, Session
from decouple import config
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv


COIN_MARKET_CAP_API_KEY = config('COIN_MARKET_CAP_API_KEY')

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'500',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COIN_MARKET_CAP_API_KEY,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data['data'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

 
 
# Opening JSON file and loading the data
# into the variable data

crypto_data = data['data']
 
# now we will open a file for writing
data_file = open('data_file.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing
# headers to the CSV file
count = 0
 
for coin in crypto_data:
    if count == 0:
 
        # Writing headers of CSV file
        header = coin.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(coin.values())
 
data_file.close()