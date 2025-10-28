import datetime
import yfinance as yf

def get_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        company_name = info.get("longName", "Unknown Company")
        current_price = info.get("currentPrice", None)
        previous_close = info.get("previousClose", None)

        if current_price is None or previous_close is None:
            print("❌ Could not retrieve stock data. Please check the symbol.")
            return

        value_change = round(current_price - previous_close, 2)
        percent_change = round((value_change / previous_close) * 100, 2)

        print(datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y"))
        print(f"{company_name} ({symbol.upper()})")

        sign_value = "+" if value_change > 0 else ""
        sign_percent = "+" if percent_change > 0 else ""
        print(f"{current_price} {sign_value}{value_change} ({sign_percent}{percent_change}%)")

    except Exception as e:
        print(f"⚠️ Error: {e}")
        print("Please check your internet connection or the stock symbol.")

if __name__ == "__main__":
    while True:
        symbol = input("\nPlease enter a symbol (or 'exit' to quit): ").strip()
        if symbol.lower() == "exit":
            break
        elif not symbol:
            print("⚠️ Please enter a valid symbol.")
            continue
        get_stock_info(symbol)
