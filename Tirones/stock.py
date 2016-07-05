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

    def getOpen(self, start=-1, end=-1):

        return self.getValue(start, end, 'Open')

    def getClose(self, start=-1, end=-1):

        return self.getValue(start, end, 'Close')

    def getValue(self, start, end, type):

        if start == -1:
            start = self.start

        if end == -1:
            end = self.end

        try:
            startIndex = self.findIndexInHist(start)

        except StopIteration:
            startIndex = 0;

        try:
            self.findIndexInHist(end)
        except StopIteration:
            ''' If end was not found (date on weekend and list does not 
                extend to next working day) set endIndex to end of list'''
            endIndex = len(self.hist)

        return [day[type] for day in self.hist[startIndex:endIndex]]

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

    def isHistEmpty(self):
        return not len(self.hist)

    def padHist(self, dates):
        if len(dates) == len(self.hist):
            return

        try:
            for i in range(0,len(dates)-1):
                while(self.hist[i]['Date'] != dates[i]):
                    self.hist.insert(i,{'Volume': '0', 'Symbol': self.symbol, 'Adj_Close': '0', 'High': '0', 'Low': '0', 'Date': dates[i], 'Close': '0', 'Open': '0'})             
        except IndexError:
            while(len(self.hist) < len(dates)):
                self.hist.append({'Volume': '0', 'Symbol': self.symbol, 'Adj_Close': '0', 'High': '0', 'Low': '0', 'Date': dates[i], 'Close': '0', 'Open': '0'})
    
    def checkDates(self, start, end):

        if self.start > start:
            raise ValueError("Start time before history start",'startbeforehist')
        elif self.end < end:
            raise ValueError("End time after history end",'endafterhist')

    def findIndexInHist(self, date):
        return next(day[0] for day in enumerate(self.hist) if self.convertTime(day[1]['Date']) >= date)

    def plot(self, plotStart, plotEnd, types=['Close'], fmt=['b-']):

        plotStart = self.convertTime(plotStart)
        plotEnd = self.convertTime(plotEnd)
        self.checkDates(plotStart, plotEnd)

        if len(types) != len(fmt):
            raise ValueError("Length of 'types' and 'fmt' must be the same. len(types): %d, len(fmt): %d" % (len(types), len(fmt)))

        # Find index in hist for plotting
        try:
            startIndex = self.findIndexInHist(plotStart)

        except StopIteration:
            startIndex = 0;

        try:
            self.findIndexInHist(plotEnd)
        except StopIteration:
            ''' If end was not found (date on weekend and list does not 
                extend to next working day) set endIndex to end of list'''
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