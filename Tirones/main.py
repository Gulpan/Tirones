import stock

def main():

    ABB = stock.stock('ABB.ST')
    ABB.getHist('2016-06-01', '2016-06-26')
    ABB.plot('2016-06-01', '2016-06-26')

if __name__ == '__main__':
    main()