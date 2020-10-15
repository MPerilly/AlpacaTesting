import alpaca_trade_api as tapi
from config import *

api = tapi.REST(API_KEY, SECRET_KEY, BASE_URL)
account = api.get_account()
print(account)
aapl_bars = api.get_barset("AAPL", "minute", 100)
print(aapl_bars)