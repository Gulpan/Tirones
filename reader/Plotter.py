from math import pi

from bokeh.plotting import figure, show, output_file

class Plotter:

    def __init__(self):
        self.TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

    def newFigure(self):
        self.p = figure(x_axis_type="datetime", tools=self.TOOLS, plot_width=1000, toolbar_location="left")

    def showFigure(self):
        show(self.p)

    def plot_stock(self, stock):
        self.p.line(stock.getDates(), stock.getClosingPrice(), color="black")
        self.p.line(stock.getDates(), stock.getRollingMean(5), color="red")

    def plot_candelStick(self, stock):

        mids = stock.getAverageDay()
        spans = stock.getDailySpan()

        inc = stock.getIncreaseDays()
        dec = stock.getDecreaseDays()
        w = 12 * 60 * 60 * 1000  # half day in ms

        self.p.segment(stock.getDates(), stock.getHighPrice(), stock.getDates(), stock.getLowPrice(), color="black")
        self.p.rect(stock.getDates()[inc], mids[inc], w, spans[inc], fill_color="#D5E1DD", line_color="black")
        self.p.rect(stock.getDates()[dec], mids[dec], w, spans[dec], fill_color="#F2583E", line_color="black")

        self.p.xaxis.major_label_orientation = pi / 4
        self.p.grid.grid_line_alpha = 0.3
