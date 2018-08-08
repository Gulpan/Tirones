from reader.Plotter import Plotter
from reader.Signaler import Signaler
from reader.Stock import Stock
from reader.config import getConfig

if __name__ == '__main__':
    plotter = Plotter()

    configs = getConfig()

    for config in configs:

        stock = Stock(config.symbol)
        stock.collectData(config.fromDate, config.toDate)

        signaler = Signaler(stock)

        tmp = signaler.slidingAverageSignal(5)

        plotter.newFigure()
        plotter.plot_stock(stock)
        plotter.newFigure()
        plotter.plot_candelStick(stock)
        plotter.showFigure()
