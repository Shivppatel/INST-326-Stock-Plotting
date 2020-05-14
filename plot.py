"""
Name: Shiv Pravin Patel
Directory ID: Spatel54
Date: 2020-05-14
Assignment: Final Project: Visualize Stock Data from an API 
"""

from matplotlib import pyplot as plt
import get_data as gd # imports file to complete data queries 
import tickers as tk
import sys

# Sets the ticker variable to the one passed in by terminal
ticker = sys.argv[1]

'''
    This method creates a plot with the price data for the past 12 months.
    This method takes in a list of dates, the closing price data for those dates,
    and the SMA for those dates as parameters. 
    If the price is currently above the 10 month SMA it will be drawen in green
    otherwise it will be red. The SMA will be drawn in black with dashed lines.
'''
def create_plot(price_date, price_data_close, sma_data_close):
    price_color = 'g' if price_data_close[-1] > sma_data_close[-1] else 'r'
    plt.plot(price_date[-12:], price_data_close[-12:], price_color,
        price_date[-12:], sma_data_close, 'k--')
    plt.xlabel('Date')
    plt.ylabel('Price($)')
    plt.title(f'{ticker} Price Data')
    plt.show()


if(ticker in tk.symbols):
    price_date, price_data_close= gd.get_stock_data_monthly(ticker)
    price_date.reverse() # reverses the data so the most recent is last
    price_data_close.reverse() # reverses the data so the most recent is last

    sma_data = gd.get_stock_sma_monthly(ticker) 
    sma_data_close = [] # list to store SMA price data for the past 12 months

    # appends the simple moving average of the last 12 months
    for date in price_date[-12:]:
        sma_data_close.append(float(sma_data[date]['SMA']))

    create_plot(price_date, price_data_close, sma_data_close)
else:
    print('Enter a valid stock thats in the S&P 500')
