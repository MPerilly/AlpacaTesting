import requests, json
from config import *
DATA_URL = "https://data.alpaca.markets/v1"
HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
TIMEFRAME = "day"
BARS_URL = "{}/v1/bars/{}".format(BASE_URL, TIMEFRAME)

def getAccount():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

