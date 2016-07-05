import sys, getopt
import stock
from readSymbols import readStockSymbols
from stockCluster import stockCluster
import datetime
import numpy as np
import pickle


def main(argv):

    inputfile = 'OMX.pkl'

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            inputfile = arg
            updateQuotes('2012-06-05','2016-06-26', outputfile)


    with open(inputfile, 'rb') as input:
        stockList = pickle.load(input)

    stockList = [company for company in stockList if len(company.hist) > 1000]

    histLen = [len(company.hist) for company in stockList]

    histMax = max(histLen)
    histMaxIndex = max(xrange(len(histLen)),key=histLen.__getitem__)

    dateCompany = stockList[0]

    dates = []
    for day in dateCompany.hist:
        dates.append(day['Date'])

    for company in stockList:
        company.padHist(dates)
    #comp = stockList[5]
    #comp.plot('2012-06-05', '2016-06-26')
 
    clust = stockCluster.stockCluster(stockList)
    clust.makeCluster()
    clust.plotCluster()


def updateQuotes(start, end, outputfile):

    dataList = readStockSymbols.readSymbols("readSymbols/large-cap.htm")

    stockList = []

    for i in range(0,len(dataList)):
        company = stock.stock(dataList[i])
        if company.name.endswith('-A') or company.name.endswith('-PREF'):
            continue

        company.getHist(start, end)
        # Only keep companies with history in the period
        if not company.isHistEmpty():
            stockList.append(company)

    with open(outputfile, 'wb') as output:
        pickle.dump(stockList, output, pickle.HIGHEST_PROTOCOL)

    del stockList

if __name__ == '__main__':
    main(sys.argv[1:])


