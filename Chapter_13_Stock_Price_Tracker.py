# Chapter_13_Stock_Price_Tracker
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and period
stock_symbol = 'AAPL'
data = yf.download(stock_symbol, start='2023-01-01', end='2023-10-15')

# Plot stock price data
plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label='Close Price')
plt.title(f'{stock_symbol} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()