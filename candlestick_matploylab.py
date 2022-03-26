import yfinance as yf 
import pandas as pd 
import mplfinance as mpf


stock = yf.download('0005.HK', period='1d', interval='1m')

data = pd.DataFrame(stock)

print(data.info())

mpf.plot(data, type='candle', volume=True)
