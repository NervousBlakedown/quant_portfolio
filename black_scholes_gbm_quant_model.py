"""This script will utilize QuantLib, a popular library for quantitative finance, 
to calculate the price of a European call option via the Black-Scholes model, 
and simulate a Geometric Brownian Motion (GBM), which is a common model 
used in finance for factors such as stock prices.

Note: The Black-Scholes model is a mathematical model used for pricing options. 
GBM is a stochastic process in which the logarithm of the randomly varying 
quantity follows a Brownian motion."""

# Imports
import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# set up the parameters for the option
valuation_date = ql.Date(26, 6, 2023)
ql.Settings.instance().evaluationDate = valuation_date
option_maturity_date = ql.Date(26, 6, 2024)
strike_price = 100
option_type = ql.Option.Call
day_count = ql.Actual365Fixed()

"""can use ql.UnitedStates.NYSE for the New York Stock Exchange
ql.UnitedStates.Settlement for the standard settlement calendar"""
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond) 

underlying_price = ql.SimpleQuote(100)
risk_free_rate = ql.SimpleQuote(0.01)  # 1% risk free rate
volatility = ql.SimpleQuote(0.2)  # 20% volatility

# construct the European option
payoff = ql.PlainVanillaPayoff(option_type, strike_price)
exercise = ql.EuropeanExercise(option_maturity_date)
european_option = ql.VanillaOption(payoff, exercise)

# construct the Black-Scholes-Merton process
risk_free_curve = ql.FlatForward(valuation_date, ql.QuoteHandle(risk_free_rate), day_count)
volatility_curve = ql.BlackConstantVol(valuation_date, calendar, ql.QuoteHandle(volatility), day_count)
bsm_process = ql.BlackScholesProcess(ql.QuoteHandle(underlying_price), ql.YieldTermStructureHandle(risk_free_curve), ql.BlackVolTermStructureHandle(volatility_curve))

# price the option
european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
bs_price = european_option.NPV()
print(f"The theoretical price of the European call option is {bs_price}")

# GBM simulation
np.random.seed(1)
T = 1.0  # time horizon
N = 100  # number of time steps
dt = T/N  # time step
mu = 0.05  # drift
sigma = 0.2  # volatility
S0 = 100  # initial stock price

S = np.zeros(N+1)
t = np.linspace(0, T, N+1)
S[0] = S0
for i in range(1, N + 1):
    dW = np.sqrt(dt) * np.random.standard_normal()  # standard normal random numbers scaled by sqrt(dt)
    S[i] = S[i-1]*np.exp((mu-0.5*sigma**2)*dt + sigma*dW)

# Plot using Plotly
fig = go.Figure(data=go.Scatter(x=t, y=S, mode='lines'))
fig.update_layout(title='Geometric Brownian Motion Simulation',
                   xaxis_title='Time (Years)',
                   yaxis_title='Stock Price')
fig.show()