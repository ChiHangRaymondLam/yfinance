from datetime import datetime
import datetime
import yfinance as yf


def yfmain(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    investment = tickerinfo['shortName']
    print('Investment: ' + investment)

    today = datetime.datetime.today().isoformat()
    # print('Today = ' + today)

    tickerDF = tickerdata.history(period='1d',start='2022-1-1',end=today[:10])
    priceLast = tickerDF['Close'].iloc[-1]
    priceVest = tickerDF['Close'].iloc[-2]
    change = priceLast - priceVest
    print(f'{investment} price last = {priceLast}')
    print(f'Price change = {change}')


yfmain('TSLA')
print('')
yfmain('VOO')
print('')
yfmain('HSBA.L')
print('')
yfmain('0700.HK')