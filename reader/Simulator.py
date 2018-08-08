from reader.Plotter import Plotter
from reader.Signaler import Signaler
from reader.Stock import Stock
from reader.config import getConfig
from datetime import timedelta, date

avg_days = 5

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

if __name__ == '__main__':
    plotter = Plotter()

    configs = getConfig()

    for config in configs:

        for currentDate in daterange(config.fromDate, config.toDate):

            stock = Stock(config.symbol)
            stock.collectData(config.fromDate, config.toDate)

            signaler = Signaler(stock)

            tmp = signaler.slidingAverageSignal(5)

            plotter.newFigure()
            plotter.plot_stock(stock)
            plotter.newFigure()
            plotter.plot_candelStick(stock)
            plotter.showFigure()
