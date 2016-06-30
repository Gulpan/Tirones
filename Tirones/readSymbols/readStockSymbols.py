
import re

def readSymbols(filename):

    f = open(filename,'r')

    keyString = "/shares/microsite?Instrument="

    dataList = []

    for line in f:
        if keyString in line:
            data = {}
            line = f.next()
            matchFirst = re.search("'>", line)
            matchSecond = re.search("</", line)
            data['Symbol'] = line[matchFirst.start(0)+2:matchSecond.start(0)]
            data['Symbol'] = re.sub(r"\s+", '-', data['Symbol'])
            dataList.append(data)

    return dataList

    f.close()


if __name__ == '__main__':
    readSymbols('large-cap.htm')