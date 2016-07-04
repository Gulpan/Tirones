import stock
from readSymbols import readStockSymbols
from stockCluster import stockCluster
import numpy as np


def main():

    dataList = readStockSymbols.readSymbols("readSymbols/large-cap.htm")

    stockList = []

    for i in range(1,10):
        company = stock.stock(dataList[i])
        company.getHist('2016-06-01', '2016-06-26')
        # Only keep companies with history in the period
        if not company.isHistEmpty():
            stockList.append(company)
    
    #openPrice = np.array([company.getOpen() for company in stockList]).astype(np.float)

    clust = stockCluster.stockCluster(stockList)
    clust.makeCluster()

if __name__ == '__main__':
    main()