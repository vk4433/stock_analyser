import yfinance as yf
from yahooquery import search

def get_stock_price(company,days):
    results = search(company).get("quotes",[])
    if not results:
        return f" No ticker found for '{company}'."
    symbol =results[0]["symbol"]
    stock = yf.Ticker(symbol)
    try:
        history =stock.history(period =f"{days}d")["Close"]

        return f" {company} ({symbol}) - Last {days} Days:\n{history.to_string()}" if not history.empty else f" No data for '{company}'."
    except Exception as e:
        return f" Error fetching stock data: {e}"
    
    
