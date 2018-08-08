import pandas as pd

from reader.Reader import Reader

class Stock:

    def __init__(self, symbol):
        self.symbol = symbol
        self.reader = Reader()

    def collectData(self, fromDate, toDate):
        self.data = self.reader.get_data(self.symbol, fromDate, toDate)
        self.data['Date'] = pd.to_datetime(self.data.T.keys())

    def getRollingMean(self, days):
        return self.getClosingPrice().rolling(days).mean()

    def getClosingPrice(self, fromDate=None, toDate=None):
        return self.__getData__('Close')

    def getOpenPrice(self, fromDate=None, toDate=None):
        return self.__getData__('Open')

    def getHighPrice(self, fromDate=None, toDate=None):
        return self.__getData__('High')

    def getLowPrice(self, fromDate=None, toDate=None):
        return self.__getData__('Low')

    def getDates(self):
        return self.__getData__('Date')

    def getIncreaseDays(self):
        return self.getClosingPrice() > self.getOpenPrice()

    def getDecreaseDays(self):
        return self.getOpenPrice() > self.getClosingPrice()

    def getAverageDay(self):
        return (self.getOpenPrice() + self.getClosingPrice()) / 2

    def getDailySpan(self):
        return abs(self.getClosingPrice() - self.getOpenPrice())

    def __getData__(self, type, fromDate=None, toDate=None):
        if not fromDate and not toDate:
            return self.data[type]
        else:
            raise ValueError("Not implemented")