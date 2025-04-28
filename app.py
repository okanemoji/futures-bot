from flask import Flask, request, jsonify
from binance_futures import FuturesTrader
import os

app = Flask(__name__)

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

trader = FuturesTrader(API_KEY, API_SECRET)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    action = data.get('action')
    symbol = data.get('symbol')
    qty = float(data.get('qty'))
    leverage = int(data.get('leverage', 10))

    if not all([action, symbol, qty]):
        return jsonify({'error': 'Invalid payload'}), 400

    try:
        trader.set_leverage(symbol, leverage)

        if action.lower() == 'buy':
            order = trader.open_long(symbol, qty)
        elif action.lower() == 'sell':
            order = trader.open_short(symbol, qty)
        else:
            return jsonify({'error': 'Invalid action'}), 400

        return jsonify({'status': 'success', 'order': order}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
