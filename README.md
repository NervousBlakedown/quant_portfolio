# quant_portfolio
My data science quant portfolio.  Conversations always welcome.


## Project I: Black-Scholes Model and Geometric Brownian Motion Model
In this example, I calculate the price of a European call option via the Black-Scholes model, and simulate a Geometric Brownian Motion (GBM), which is a common model used in finance for factors such as stock prices.

_Note: The Black-Scholes model is a mathematical model used for pricing options. GBM is a stochastic process in which the logarithm of the randomly varying quantity follows a Brownian motion._

### Black-Scholes, GBM Model Summary
The Geometric Brownian Motion is used to model the random evolution of a stock price over time in the Black-Scholes option pricing model and other financial models. The randomness (Brownian motion part) is necessary as stock prices in real-world markets are influenced by many unpredictable factors.

### Line Chart Description
X Coordinate (Time (Years)): This represents the time evolution of the Geometric Brownian Motion (GBM). It starts from 0 (the start of our simulation) and goes to 1, representing a one-year time horizon. The time is divided into 100 steps (N = 100), which means the time increment (dt = T/N) is 0.01 years or about 3.65 days.

Y Coordinate (Stock Price): This represents the simulated stock price at each point in time according to the GBM. The initial stock price (S0 = 100) is set at the start of the simulation. At each time step, the new stock price is determined by the previous stock price multiplied by an exponential term, which includes the drift term (mu = 0.05, which can be considered as the expected return of the stock), the volatility term (sigma = 0.2), and a standard normal random number (dW), which introduces randomness into the stock price evolution.


## Project II: Credit Risk Assessment: Credit Risk Model
For this example, I have generated random data that would be used for a quant credit risk situation (customer ID's for an index value, age, income, loan amount, and a boolean that states whether each customer defaulted on their loan or not).  I then set up a logistic regression model on this data and visualize the results in a 3D Scatterplot within Plotly.


## Project III: Market Risk Model: VaR
This example calculates the Value-at-Risk (VaR) and visualize the cumulative returns of a portfolio of stocks. It utilizes historical price data obtained from Yahoo Finance using the yfinance library and performs various calculations using numpy, pandas, scipy, and plotly.graph_objs.

### Portfolio Definition
The script begins by defining the portfolio, which consists of a list of stock tickers and their corresponding weights. In this example, the portfolio includes Apple (AAPL), Google (GOOGL), Microsoft (MSFT), and Amazon (AMZN) with equal weights.

### Historical Data Retrieval
Next, the script downloads the adjusted closing prices of the stocks within the specified time range (from 'start_date' to 'end_date'). The data is stored in a pandas DataFrame for further analysis.

### Return Calculation
The script calculates the daily returns of each stock by using the pct_change() function provided by pandas. Then, it computes the portfolio returns by taking the dot product of the returns and the weight vector.

### VaR Calculation
VaR is a risk measure that estimates the potential loss of a portfolio over a given time horizon at a certain confidence level. The script calculates VaR using the percentile function from numpy. The confidence level is set to 95% (or 0.05), but it can be adjusted as needed. The negative value of VaR is printed as the output.

### Cumulative Returns Visualization
The script plots the cumulative returns of the portfolio over time using the plotly library. It also calculates and includes a best-fit line using linear regression to visualize the trend in the portfolio's performance. Additionally, it plots a dashed line representing the VaR at the chosen confidence level.

### Additional Line Options
The script suggests two additional line options that can be included in the line graph for further analysis. The first option is to add a line representing the cumulative returns of a benchmark index, such as the S&P 500, to compare the portfolio's performance against the overall market. The second option is to plot lines representing the portfolio's moving averages, which can help identify trends over different time frames.

### Chart Layout
The script defines the layout for the line graph, including the title, axes labels, and annotations. The title dynamically includes the names of the stocks in the portfolio. It also provides information about the date range of the historical data used.

### Output
Finally, the script generates the line graph using the go.Figure() function from plotly and displays it using fig.show().

By using this script, users can analyze the VaR of their portfolio and visualize its cumulative returns, allowing them to make informed investment decisions based on risk assessment and performance evaluation.


