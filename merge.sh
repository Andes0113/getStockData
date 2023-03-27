#!/bin/bash

echo "date,open,high,low,close,volume,Ticker" > stock_data.csv
cd individual
files=$(ls *.csv)
for file in $files
do
	tail -n +2 $file >> ../stock_data.csv
done