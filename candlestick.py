# Period
# Options: 1d 5d 1 wk 1mo 3mo 6mo 1y 2y 5y 10y

# Interval
# Options: 1m 2m 5m 15m 30m 60m 90m 
 
import yfinance as yf 
import pandas as pd 
import plotly.graph_objects as pg 


stock = yf.download('0005.HK', period='1d', interval='1m')

data = stock.reset_index()

data.columns = ['Current Time', 'Opening Price', 'Highest Price', 'Lowest Price', 'Closing Price', 'Adjusted Closing Price', 'Volume']
data['Current Time'] = pd.to_datetime(data['Current Time'].dt.strftime('%Y-%m-%d %H:%M'))
data['Volume'] //= 1000

result = pg.Figure()

# Volume Graph
result.add_trace(
    pg.Bar(
        name = 'Volume',
        x = data['Current Time'],
        y = data['Volume'],
        yaxis = 'y2',
        marker_color = '#99ccff'
    )
)

# Candlestick Graph
result.add_trace(
    pg.Candlestick(
        name = '',
        x = data['Current Time'],
        open = data['Opening Price'],
        high = data['Highest Price'],
        low = data['Lowest Price'],
        close = data['Closing Price'],
        increasing_line_color = '#fd5047',
        increasing_fillcolor = '#f29696',
        decreasing_line_color = '#3d9970',
        decreasing_fillcolor = '#91c2b3'
    )
)

result.update_layout(
    title = '0005 HSBC',
    hovermode = 'x unified', # Showing information when the mouse hover on the graph

    yaxis = dict(
        title = 'Stock Price'
    ),

    yaxis2 = dict(
        overlaying = 'y',
        visible = False
    ),

    font = dict(
        size = 20
    )
)

result.show()