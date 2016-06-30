
import re

def readSymbols(filename):

    f = open(filename)

    keyString = "/shares/microsite?Instrument="

    symbols = []

    for line in f:
        if keyString in line:
            line = f.next()
            matchFirst = re.search("'>", line)
            matchSecond = re.search("</", line)
            symbol = line[matchFirst.start(0)+2:matchSecond.start(0)]
            symbol = re.sub(r"\s+", '-', symbol)
            symbols.append(symbol)

    return symbols

    f.close()


if __name__ == '__main__':
    readSymbols('large-cap.htm')