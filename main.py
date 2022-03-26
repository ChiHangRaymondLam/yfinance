from datetime import datetime
import datetime
import yfinance as yf

# The 100 most active stocks in New Zealand
# url = 'https://nz.finance.yahoo.com/most-active?offset=0&count=100'

def yfmain(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    investment = tickerinfo['shortName']
    print(f'Investment: {investment}')

    today = datetime.datetime.today().isoformat()

    tickerDF = tickerdata.history(period='1d',start='2022-1-1',end=today[:10])
    priceLast = tickerDF['Close'].iloc[-1]
    priceVest = tickerDF['Close'].iloc[-2]
    change = priceLast - priceVest
    print(f'{investment} price last = {priceLast}')
    print(f'Price change = {change}')

# Ticker symbol example: 'TSLA', 'AMZN', 'AAPL', '0005.HK', '0700.HK'
print('This application helps you to check the latest prices and spreads of stocks.')
symbol = input('Input the ticker symbol: ')

yfmain(symbol)
