import datetime

class stockConfig:

    def __init__(self, symbol, fromDate, toDate, **kwargs):
        self.symbol = symbol
        self.fromDate = fromDate
        self.toDate = toDate
        self.kwargs = kwargs

def getConfig():

    config = [
        stockConfig('SWDBY', datetime.datetime(2017, 7, 1), datetime.datetime(2018, 7, 21))
    ]

    return config