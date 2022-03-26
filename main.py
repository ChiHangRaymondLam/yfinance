import requests
import pandas as pd
import yfinance as yf

# url = 'https://finance.yahoo.com/screener/predefined/most_actives?offset=0&count=100'
# data = pd.read_html(url)[0]

def yfmain(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    print(tickerinfo)

yfmain('TSLA')