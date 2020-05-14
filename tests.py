import unittest
import get_data as gd
import tickers as tk
# Check to make sure we are getting back back from the api
assert gd.get_stock_data_monthly('AAPL') is not None

# Makes sure that the Simple moving average data recive is in the type dict
assert type(gd.get_stock_sma_monthly('AAPL')) == dict

# Makes sure that the stock price data is converted to type float
assert type(gd.get_stock_data_monthly('AAPL')[1][0]) == float

# Makes sure there are an even ammount of date data and price data
assert len(gd.get_stock_data_monthly('AAPL')[0]) == len(gd.get_stock_data_monthly('AAPL')[0]) 

# Makes sure that the program is checking to see if the stock is in the s&p 500
assert 'TSLA' not in tk.symbols
