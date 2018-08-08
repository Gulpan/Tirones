import pandas_datareader.data as web
import fix_yahoo_finance as yf
yf.pdr_override()
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols

class Reader:

    def get_data(self, symbol, start, end):
        #return web.get_data_morningstar(symbol, start, end)
        return web.DataReader(symbol, 'google', start, end)