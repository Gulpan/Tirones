import stock
from readSymbols import readStockSymbols

def main():

    dataList = readStockSymbols.readSymbols("readSymbols/large-cap.htm")
    print dataList[15]['Symbol']
    ABB = stock.stock(dataList[15]['Symbol']+".ST")

    ABB.getHist('2016-05-01', '2016-06-26')
    ABB.plot('2016-06-02', '2016-06-26',['Close','High','Low'],['b-','r--','r--'])

if __name__ == '__main__':
    main()