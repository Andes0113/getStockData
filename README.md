# getStockData

This repository is an extension of a [script by CNuge](https://github.com/CNuge/kaggle-code/tree/master/stock_data). Many thanks to you for 

Reasons for changes:
* In the original file, the use of pandas_datareader causes an error. I have switched to yfinance to prevent this issue.
* Changed from hardcoded stocks to file input to allow for downloading of any stock data.
* Migrated from multithreading to a single thread to avoid rate limits with yfinance. Big drop in performance, but unfortunately necessary in current form. 

stocks.txt consists of stocks from the S&P500, sourced from [a dataset on github](https://github.com/datasets/s-and-p-500-companies/blob/master/data/constituents_symbols.txt).
