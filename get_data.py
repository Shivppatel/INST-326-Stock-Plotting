"""
Name: Shiv Pravin Patel
Directory ID: Spatel54
Date: 2020-05-01
Assignment: Homework 5: Visualize Data from an API 
"""

import requests
import json

KEY = '1ZGOVMAENI06HLTN' # Alpha Vantage API key
URL = 'https://www.alphavantage.co/query?function=' # API base url


'''
    This method takes in a stock ticker as an argument and returns two lists.
    The first list contians dates for the corosponding closing price list.
'''
def get_stock_data_monthly(ticker):
    price_url = URL + 'TIME_SERIES_MONTHLY_ADJUSTED&symbol={}&apikey={}'.format(ticker, KEY)
    data = requests.get(price_url).json()
    data = data['Monthly Adjusted Time Series']
    price_data_close = []
    price_date = []
    for line in data.keys():
        price_date.append(line)
        price_data_close.append(float(data[line]['4. close']))
    return price_date, price_data_close


'''
    This method takes in a stock ticker as an arugumnet and returns a dict of 
    10 month Simple Moving Average data with the key being the date.
'''
def get_stock_sma_monthly(ticker):
    price_url = URL + 'SMA&symbol={}&interval=monthly&time_period=10&series_type=close&apikey={}'.format(ticker, KEY)
    data = requests.get(price_url).json()
    return data['Technical Analysis: SMA']