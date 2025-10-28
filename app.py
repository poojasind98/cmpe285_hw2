from flask import Flask, request, jsonify
import logic  # or directly copy your code here

app = Flask(__name__)

@app.route('/api/stock', methods=['GET'])
def stock_data():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"error": "Stock symbol required"}), 400
    try:
        data = logic.get_stock_data(symbol)  # call your existing logic
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return open("index.html").read()
