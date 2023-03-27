# getStockData

## Flexible stock fetching script

### To run:
* python -m venv venv
* source venv/bin/activate
* python -m pip install -U pandas_datareader yfinance
* python getStockData.py
* bash merge.sh

Voila, you now have the data from all of your stocks in stock_data.csv and individual stocks in individual/[ticker]_data.csv

### This repository is an extension of a [script by CNuge](https://github.com/CNuge/kaggle-code/tree/master/stock_data) for my personal use case.

Changes and Reasoning:
* In the original file, the use of pandas_datareader causes an error. I have switched to yfinance to prevent this issue.
* Changed from hardcoded stocks to file input to allow for downloading of any stock data.
* Migrated from multithreading to a single thread to avoid rate limits with yfinance. Big drop in performance, but unfortunately necessary in current form.
* In csv files, changed Name -> Ticker. This is just for my use case.

stocks.txt consists of stocks from the S&P500, sourced from [a dataset on github](https://github.com/datasets/s-and-p-500-companies/blob/master/data/constituents_symbols.txt).
