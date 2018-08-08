import numpy as np

from reader.Signal import Signal

class Signaler:

    def __init__(self, stock):
        self.stock = stock

    def slidingAverageSignal(self, days):
        slidingAverage = self.stock.getRollingMean(days)

        intersections = self.__findIntersections__(slidingAverage)

        if intersections.keys()[-1] == self.stock.getDates().iloc[-1]:
            if slidingAverage.iloc[-1] > self.stock.getClosingPrice().iloc[-1]:
                return Signal.SELL
            else:
                return Signal.BUY

        return None


    def __findIntersections__(self, values):

        diff = self.stock.getClosingPrice() - values

        cross = np.sign(diff.shift(1)) != np.sign(diff)

        return cross[cross]