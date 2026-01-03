from binance.client import Client
from config import API_KEY, API_SECRET

client = Client(API_KEY, API_SECRET)

def get_klines(symbol, interval, limit=500):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    return klines

def market_buy(symbol, qty):
    return client.order_market_buy(symbol=symbol, quantity=qty)

def market_sell(symbol, qty):
    return client.order_market_sell(symbol=symbol, quantity=qty)
