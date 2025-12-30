import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Apple = yf.download("AAPL", start="2020-01-01", end="2025-01-01")
Apple.head()

ticker = ["QQQM", "VOO", "IYW"]
stocks = yf.download(ticker, start="2020-01-01", end="2025-01-01")
stocks.info()
stocks.to_csv("stocksintro.csv")
stocks = pd.read_csv("stocksintro.csv")
stocks.head()

stocks = pd.read_csv("stocksintro.csv", header=[0,1])
stocks

stocks = pd.read_csv("stocksintro.csv", header=[0,1], index_col=[0])
stocks

stocks = pd.read_csv("stocksintro.csv", header=[0,1], index_col=[0], parse_dates=[0])
stocks

stocks.columns
# convert multiindex to one tuple
stocks.columns = stocks.columns.to_flat_index()
stocks.columns
stocks
# convert back to multiindex
stocks.columns = pd.MultiIndex.from_tuples(stocks.columns)
stocks