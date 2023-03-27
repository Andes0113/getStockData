from datetime import datetime
from concurrent import futures

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

QUERY_YEARS = 5
QUERY_MONTHS = 0
QUERY_DAYS = 0

def download_stock(stock):
    """ try to query the iex for a stock, if failed note with print """
    try:
        print(stock)
        stock_df = pdr.get_data_yahoo(stock, start=start_time, end=now_time)
        stock_df['Ticker'] = stock # Changed to Ticker for my personal use case
        output_name = stock + '_data.csv'
        stock_df.to_csv('individual/' + output_name)

    except Exception as err:
        bad_names.append(stock)
        print('bad: %s' % (stock))
        print(err)

if __name__ == '__main__':

    """ set the download window """
    now_time = datetime.now()
    start_time = datetime(now_time.year - QUERY_YEARS, now_time.month - QUERY_MONTHS , now_time.day - QUERY_DAYS)

    """ get list of stocks from file """
    with open('stocks.txt', 'r') as f:
        stocks = f.read().splitlines()
	
		
    bad_names = [] #to keep track of failed queries

    """here we use the concurrent.futures module's ThreadPoolExecutor
        to speed up the downloads by doing them in parallel 
        as opposed to sequentially 
        NOTE: I am keeping this old multithreaded code for clarity about changes I've made"""

    #set the maximum thread number
    # max_workers = 50

    # workers = min(max_workers, len(stocks)) #in case a smaller number of stocks than threads was passed in
    # with futures.ThreadPoolExecutor(workers) as executor:
    #   res = executor.map(download_stock, stocks)

    # Don't multithread to ensure no rate limit issues. Unfortunately far slower but will succeed.
    # Dividing ToE by 50 would be nice, but getting the data here isn't time-sensitive, so no big deal.
    for s in stocks:
        download_stock(s)

	
    """ Save failed queries to a text file to retry """
    if len(bad_names) > 0:
        with open('failed_queries.txt','w') as outfile:
            for name in bad_names:
                outfile.write(name+'\n')

	#timing:
    finish_time = datetime.now()
    duration = finish_time - now_time
    minutes, seconds = divmod(duration.seconds, 60)
    print('getStockData.py')
    print(f'The threaded script took {minutes} minutes and {seconds} seconds to run.')
    #The threaded script took 2 minutes and 16 seconds to run.