import yahoo_finance
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dat
import datetime

class stock:
    """docstring for stock"""

    def __init__(self, stockSymbol):
        #super(stock, self).__init__()
        self.symbol = stockSymbol

    def getHist(self, start, end):
        self.yahooHandle = yahoo_finance.Share(self.symbol)
        self.hist = self.yahooHandle.get_historical(start, end)

        #self.closings = [day['Close'] for day in hist]

    def plot(self, start, end, type='Close'):

        xvalue = [day[type] for day in self.hist]
        dates = [datetime.datetime.strptime(day['Date'],"%Y-%m-%d") for day in self.hist]

        days = dat.DayLocator(tz=None, bymonthday=None, interval=2)
        daysFmt = dat.DateFormatter("%d-%m-%y")

        fig, ax = plt.subplots()
        ax.plot_date(dates, xvalue, fmt='b-')

        # TODO: Make adjustable depending on range
        ax.xaxis.set_major_locator(days)
        ax.xaxis.set_major_formatter(daysFmt)
        ax.xaxis.set_minor_locator(days)
        ax.autoscale_view()
        ax.grid(True)
        ax.set_xlabel('Date')
        ax.set_ylabel('Closing Price (SEK)')
        ax.set_title('ABB.ST')

        fig.autofmt_xdate()

        plt.show()