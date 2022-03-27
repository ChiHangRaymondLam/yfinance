# Period
# Options: 1d 5d 1 wk 1mo 3mo 6mo 1y 2y 5y 10y

# Interval
# Options: 1m 2m 5m 15m 30m 60m 90m 
 
import yfinance as yf 
import pandas as pd 
import plotly.graph_objects as go


stock = yf.download('0005.HK', period='1d', interval='1m')

data = stock.reset_index()

data.columns = ['Current Time', 'Opening Price', 'Highest Price', 'Lowest Price', 'Closing Price', 'Adjusted Closing Price', 'Volume']
data['Current Time'] = pd.to_datetime(data['Current Time'].dt.strftime('%y-%m-%d %H:%M'))
data['Volume'] //= 1000

# data['20wma'] = data['Closing Price'].rolling(window=140).mean()

fig = go.Figure()

# Volume Graph
fig.add_trace(
    go.Bar(
        name = 'Volume',
        x = data['Current Time'],
        y = data['Volume'],
        yaxis = 'y2',
        marker_color = '#0099ff'
    )
)

# Candlestick Graph
fig.add_trace(
    go.Candlestick(
        name = '',
        x = data['Current Time'],
        open = data['Opening Price'],
        high = data['Highest Price'],
        low = data['Lowest Price'],
        close = data['Closing Price'],
        increasing_line_color = '#fa3838',
        increasing_fillcolor = '#ea0606',
        decreasing_line_color = '#05e105',
        decreasing_fillcolor = '#03a003'
    )
)

# fig.add_trace(
#     go.Scatter(
#         x = data['Current Time'],
#         y = data['20wma'],
#         line = dict(color = '#e0e0e0'),
#         name = '20-week MA'
#     )
# )


fig.update_layout(
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

fig.show()