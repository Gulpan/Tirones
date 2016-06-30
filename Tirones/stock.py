import yahoo_finance
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dat
import datetime

class stock:
    """Class stock, contains all data for the stock-company"""

    def __init__(self, stockSymbol):
        #super(stock, self).__init__()
        self.symbol = stockSymbol

    def convertTime(self, time):
        return datetime.datetime.strptime(time,"%Y-%m-%d")

    def getHist(self, start, end):
        if isinstance(start, datetime.date):
            self.start = start
        else:
            self.start = self.convertTime(start)

        if isinstance(end, datetime.date):
            self.end = end
        else:
            self.end = self.convertTime(end)

        self.yahooHandle = yahoo_finance.Share(self.symbol)
        self.hist = self.yahooHandle.get_historical(self.start.strftime("%Y-%m-%d"), self.end.strftime("%Y-%m-%d"))

        #self.closings = [day['Close'] for day in hist]

    def checkDates(self, start, end):

        if self.start > self.convertTime(start):
            raise ValueError("Start time before history start",'startbeforehist')
        elif self.end < self.convertTime(end):
            raise ValueError("End time after history end",'endafterhist')


    def plot(self, start, end, types=['Close'], fmt=['b-']):

        self.checkDates(start, end)

        if len(types) != len(fmt):
            raise ValueError("Length of 'types' and 'fmt' must be the same. len(types): %d, len(fmt): %d" % (len(types), len(fmt)))

        fig, ax = plt.subplots()

        for index, type in enumerate(types):

            # TODO (BUG): Will always plot entire history
            xvalue = [day[type] for day in self.hist]
            dates = [self.convertTime(day['Date']) for day in self.hist]

            days = dat.DayLocator(tz=None, bymonthday=None, interval=2)
            daysFmt = dat.DateFormatter("%d-%m-%y")

            ax.plot_date(dates, xvalue, fmt[index])


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