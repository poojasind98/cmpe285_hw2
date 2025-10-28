from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/test')
def test():
    return "✅ Flask is running correctly!"

@app.route('/api/run', methods=['GET'])
def run_script():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"error": "Please provide a stock symbol, e.g. ?symbol=AAPL"}), 400

    try:
        # Run your existing script with subprocess and capture its output
        result = subprocess.run(
            ['python3', 'CMPE285_HW2.py'],
            input=f"{symbol}\nexit\n",
            text=True,
            capture_output=True,
            timeout=20
        )
        return f"<pre>{result.stdout}</pre>"
    except subprocess.TimeoutExpired:
        return "<pre>⚠️ Error: The request took too long. Please try again.</pre>"
    except Exception as e:
        return f"<pre>⚠️ Error: {e}</pre>"

@app.route('/')
def home():
    return open("index.html").read()

if __name__ == "__main__":
    app.run(debug=True)
