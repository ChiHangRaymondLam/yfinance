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
    print(f'{investment} price last = {str(priceLast)}')


yfmain('TSLA')
print('')
yfmain('VOO')