# quant_portfolio
My data science quant portfolio.  Conversations always welcome.

## Black-Scholes Model and Geometric Brownian Motion Model
In this example, I calculate the price of a European call option via the Black-Scholes model, and simulate a Geometric Brownian Motion (GBM), which is a common model used in finance for factors such as stock prices.

_Note: The Black-Scholes model is a mathematical model used for pricing options. GBM is a stochastic process in which the logarithm of the randomly varying quantity follows a Brownian motion._

## Summary
The Geometric Brownian Motion is used to model the random evolution of a stock price over time in the Black-Scholes option pricing model and other financial models. The randomness (Brownian motion part) is necessary as stock prices in real-world markets are influenced by many unpredictable factors.

### Line Chart Description
X Coordinate (Time (Years)): This represents the time evolution of the Geometric Brownian Motion (GBM). It starts from 0 (the start of our simulation) and goes to 1, representing a one-year time horizon. The time is divided into 100 steps (N = 100), which means the time increment (dt = T/N) is 0.01 years or about 3.65 days.

Y Coordinate (Stock Price): This represents the simulated stock price at each point in time according to the GBM. The initial stock price (S0 = 100) is set at the start of the simulation. At each time step, the new stock price is determined by the previous stock price multiplied by an exponential term, which includes the drift term (mu = 0.05, which can be considered as the expected return of the stock), the volatility term (sigma = 0.2), and a standard normal random number (dW), which introduces randomness into the stock price evolution.





