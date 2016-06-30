
import re

def helpRead(line, subFirst, subSecond):
    matchFirst = re.search(subFirst, line)
    matchSecond = re.search(subSecond, line)
    tmp = line[matchFirst.start(0)+2:matchSecond.start(0)]
    return re.sub(r"\s+", '-', tmp)

def readSymbols(filename):

    f = open(filename,'r')

    keyString = "/shares/microsite?Instrument="

    dataList = []

    for line in f:
        if keyString in line:
            data = {}

            # Read name
            data['Name'] = helpRead(line, '">', "</")

            # Read symbol
            line = f.next()
            data['Symbol'] = helpRead(line, "'>", "</")

            # Read currency
            line = f.next()
            data['Currency'] = helpRead(line, "'>", "</")

            # Read branch
            line = f.next()
            line = f.next()
            data['Branch'] = helpRead(line, "'>", "</")

            dataList.append(data)

    return dataList

    f.close()


if __name__ == '__main__':
    readSymbols('large-cap.htm')