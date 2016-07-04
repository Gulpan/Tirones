import stock
from readSymbols import readStockSymbols

def main():

    dataList = readStockSymbols.readSymbols("readSymbols/large-cap.htm")

    ABB = stock.stock(dataList[5])

    ABB.getHist('2016-06-01', '2016-06-26')
    ABB.plot('2016-06-01', '2016-06-26',['Close','High','Low'],['b-','r--','r--'])

if __name__ == '__main__':
    main()