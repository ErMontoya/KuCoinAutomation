import json
import os
import threading
import time
from kucoin.client import Margin, Market
 
marketClient = Market(api_key, api_secret,passphrase)

def isQuoteCurrency(symbol, expectedQuote):
	symbolIdx = len(symbol)-1
	quoteIdx = len(expectedQuote)-1
	equal = True
	while (equal and quoteIdx>=0):
		equal = symbol[symbolIdx]==expectedQuote[quoteIdx]
		symbolIdx= symbolIdx-1
		quoteIdx= quoteIdx-1
	return equal

def getQuoteCurrency(allCoins):
	quotes = ['USDT','BTC','ETH']
	usdtCoins = []
	for i in allCoins:
		if(isQuoteCurrency(i['symbol'],quotes[0])):
			coinAndPrice = [i['symbol'],i['last']]
			usdtCoins.append(coinAndPrice)
	return sorted(usdtCoins, key=lambda x:x[0])
	
def printCoinsAndPrice(coinsAndPrice):
	for i in coinsAndPrice:
		print(i[0])
		print(i[1])

printCoinsAndPrice(getQuoteCurrency(marketClient.get_all_tickers()['ticker']))
