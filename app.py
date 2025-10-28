from flask import Flask, request, jsonify
from CMPE285_HW2 import get_stock_info
from io import StringIO
import sys

app = Flask(__name__)

@app.route('/api/run', methods=['GET'])
def run_script():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"error": "Please provide a stock symbol, e.g. ?symbol=AAPL"}), 400

    # Capture the printed output from your get_stock_info() function
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    try:
        get_stock_info(symbol)
        sys.stdout = old_stdout
        output = mystdout.getvalue()
        return f"<pre>{output}</pre>"
    except Exception as e:
        sys.stdout = old_stdout
        return f"<pre>⚠️ Error: {e}</pre>"

@app.route('/')
def home():
    return open("index.html").read()

if __name__ == "__main__":
    app.run(debug=True)
