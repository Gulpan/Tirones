
import yahoo_finance
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dat
import datetime

def main():
    ABB = yahoo_finance.Share('ABB.ST')
    hist = ABB.get_historical('2016-06-01','2016-06-26')
    print ABB.get_trade_datetime() # In UTC (GMT +0)
    print ABB.get_open();


    closings = [day['Close'] for day in hist]
    dates = [datetime.datetime.strptime(day['Date'],"%Y-%m-%d") for day in hist]

    days = dat.DayLocator(tz=None, bymonthday=None, interval=2)
    daysFmt = dat.DateFormatter("%d-%m-%y")
    #plt.plot(closings)
    #plt.show()

    fig, ax = plt.subplots()
    ax.plot_date(dates, closings, fmt='-')
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(daysFmt)
    ax.xaxis.set_minor_locator(days)
    ax.autoscale_view()
    ax.grid(True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price (SEK)')
    ax.set_title('ABB.ST')

    fig.autofmt_xdate()

    plt.show()

if __name__ == '__main__':
    main()