from binance.client import Client

class FuturesTrader:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = 'https://fapi.binance.com/fapi'
    
    def set_leverage(self, symbol, leverage):
        self.client.futures_change_leverage(symbol=symbol, leverage=leverage)
    
    def open_long(self, symbol, quantity):
        order = self.client.futures_create_order(
            symbol=symbol,
            side='BUY',
            type='MARKET',
            quantity=quantity
        )
        return order
    
    def open_short(self, symbol, quantity):
        order = self.client.futures_create_order(
            symbol=symbol,
            side='SELL',
            type='MARKET',
            quantity=quantity
        )
        return order
