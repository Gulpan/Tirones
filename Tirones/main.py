import stock

def main():

    ABB = stock.stock('ASSA-B.ST')
    ABB.getHist('2016-05-01', '2016-06-26')
    ABB.plot('2016-05-01', '2016-06-26',['Close','High','Low'],['b-','r--','r--'])

if __name__ == '__main__':
    main()