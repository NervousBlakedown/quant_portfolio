"""Market Risk Model: VaR"""

# Imports
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from scipy import stats

# Define the portfolio
stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']  # Add or remove tickers as per the portfolio
weights = np.array([0.25, 0.25, 0.25, 0.25])  # Weights of the stocks in the portfolio

# Download historical data (YYYY-MM-DD format)
start_date = '2022-01-01'
end_date = '2023-06-26'
df = yf.download(stocks, start=start_date, end=end_date)['Adj Close']

# Calculate returns
returns = df.pct_change()

# Calculate portfolio returns
portfolio_returns = returns.dot(weights)

# Drop the NaN values from our calculated returns
portfolio_returns = portfolio_returns.dropna()

# Calculate VaR (reference confidence interval notes as needed)
confidence_level = 0.05
VaR = np.percentile(portfolio_returns, 100 * (1-confidence_level))

print('Value-at-Risk (VaR) at a confidence level of ', (1-confidence_level)*100, '% : ', -VaR)

# Calculate the cumulative returns
cumulative_returns = (1 + portfolio_returns).cumprod()

# Calculate the regression line (best fit line)
slope, intercept, r_value, p_value, std_err = stats.linregress(np.arange(len(cumulative_returns)), cumulative_returns)
best_fit_line = intercept + slope * np.arange(len(cumulative_returns))

trace0 = go.Scatter(
    x = cumulative_returns.index,
    y = cumulative_returns,
    mode = 'lines',
    name = 'Cumulative Returns'
)

trace1 = go.Scatter(
    x = cumulative_returns.index,
    y = best_fit_line,
    mode = 'lines',
    name = 'Best Fit Line',
    line = {'color': 'red'}
)

trace2 = go.Scatter(
    x = [cumulative_returns.index[0], cumulative_returns.index[-1]],
    y = [1 - VaR, (1 - VaR) * cumulative_returns.iloc[-1]],
    mode = 'lines',
    name = 'Value-at-Risk (VaR) at {}% confidence level'.format((1-confidence_level)*100),
    line = {'dash': 'dash'}
)

data = [trace0, trace1, trace2]

# Join stock names with comma
stock_names = ', '.join(stocks)

# Chart layout
layout = go.Layout(
    title = {
        'text': f"Portfolio Cumulative Returns, Best Fit Line and VaR for {stock_names}",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    titlefont = {'size': 20},
    yaxis = {'title': 'Value'},
    xaxis = {'title': 'Date'},
    annotations=[
        dict(
            x=0.5,
            y=0.85,
            showarrow=False,
            text='Date Range: {} to {}'.format(start_date, end_date),
            xref="paper",
            yref="paper",
            font=dict(size=14),
            align='center'
        )
    ]
)

fig = go.Figure(data=data, layout=layout)
fig.show()

"""other line options for line graph: 1.) a line representing the cumulative returns 
of a benchmark index like the S&P 500 to compare the performance 
of the portfolio with the overall market. 
2.) lines representing the portfolio's moving average to 
identify trends over different time frames."""


