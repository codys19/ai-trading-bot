import ccxt
import time

# Configure API keys (replace with your actual keys)
api_key = "your_binance_api_key"
api_secret = "your_binance_api_secret"

# Initialize Binance exchange
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True
})

# Trading parameters
symbol = 'BTC/USDT'  # Change this to any trading pair
trade_amount = 0.001  # Example trade size
profit_target = 1.01  # 1% profit target
stop_loss = 0.99  # 1% stop loss

def get_price():
    """Fetches the latest market price"""
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def place_order(order_type):
    """Places a market order"""
    if order_type == "buy":
        order = exchange.create_market_buy_order(symbol, trade_amount)
    elif order_type == "sell":
        order = exchange.create_market_sell_order(symbol, trade_amount)
    return order

# Example strategy loop
while True:
    try:
        current_price = get_price()
        print(f"Current price: {current_price}")

        # Example: If price drops 2%, buy; if price increases 2%, sell
        if current_price < get_price() * stop_loss:
            print("Placing Buy Order...")
            place_order("buy")

        elif current_price > get_price() * profit_target:
            print("Placing Sell Order...")
            place_order("sell")

        time.sleep(10)  # Wait 10 seconds before checking again

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
