from flask import Flask, jsonify, request
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

@app.route('/api/stock')
def get_stock():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"error": "No symbol provided"}), 400
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        data = {
            "datetime": datetime.now().strftime("%a %b %d %H:%M:%S"),
            "name": info.get("longName", "N/A"),
            "price": info.get("currentPrice", "N/A"),
            "change": info.get("regularMarketChange", "N/A"),
            "percent_change": info.get("regularMarketChangePercent", "N/A")
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
