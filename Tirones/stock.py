import yahoo_finance
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dat
import datetime

class stock:
    """Class stock, contains all data for the stock-company"""

    def __init__(self, data):
        #super(stock, self).__init__()
        self.symbol = data['Symbol'] + '.ST'
        self.name = data['Name']
        self.branch = data['Branch']
        self.currency = data['Currency']

    def convertTime(self, time):
        if not isinstance(time, datetime.date):
            return datetime.datetime.strptime(time,"%Y-%m-%d")
        else:
            return time

    def getHist(self, start, end):

        self.start = self.convertTime(start)
        self.end = self.convertTime(end)

        self.yahooHandle = yahoo_finance.Share(self.symbol)
        self.hist = list(reversed(self.yahooHandle.get_historical(self.start.strftime("%Y-%m-%d"), self.end.strftime("%Y-%m-%d"))))
        #self.closings = [day['Close'] for day in hist]

    def checkDates(self, start, end):

        if self.start > start:
            raise ValueError("Start time before history start",'startbeforehist')
        elif self.end < end:
            raise ValueError("End time after history end",'endafterhist')


    def plot(self, plotStart, plotEnd, types=['Close'], fmt=['b-']):

        plotStart = self.convertTime(plotStart)
        plotEnd = self.convertTime(plotEnd)
        self.checkDates(plotStart, plotEnd)

        if len(types) != len(fmt):
            raise ValueError("Length of 'types' and 'fmt' must be the same. len(types): %d, len(fmt): %d" % (len(types), len(fmt)))


        # Find index in hist for plotting
        startIndex = next(day[0] for day in enumerate(self.hist) if self.convertTime(day[1]['Date']) >= plotStart)

        ''' If end was not found (date on weekend and list does not 
            extend to next working day) set endIndex to end of list'''
        #endIndex = len(self.hist)

        try:
            endIndex = next(day[0] for day in enumerate(self.hist) if self.convertTime(day[1]['Date']) >= plotEnd)
        except StopIteration:
            endIndex = len(self.hist)

        # Create figure
        fig, ax = plt.subplots()

        # Plot
        for index, type in enumerate(types):

            xvalue = [day[type] for day in self.hist[startIndex:endIndex]]
            dates = [self.convertTime(day['Date']) for day in self.hist[startIndex:endIndex]]

            ax.plot_date(dates, xvalue, fmt[index])

        numXLabels = 10
        interval = (endIndex - startIndex)/numXLabels + 1
        # Set format for xlabel
        days = dat.DayLocator(tz=None, bymonthday=None, interval=interval)
        daysFmt = dat.DateFormatter("%d-%m-%y")

        # Set axis values
        ax.xaxis.set_major_locator(days)
        ax.xaxis.set_major_formatter(daysFmt)
        ax.xaxis.set_minor_locator(days)
        ax.autoscale_view()
        ax.grid(True)
        ax.set_xlabel('Date')
        ax.set_ylabel('Closing Price (' + self.currency + ')')
        ax.set_title(self.symbol)

        fig.autofmt_xdate()

        plt.show()