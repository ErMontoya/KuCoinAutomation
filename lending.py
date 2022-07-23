import json
import os
import threading
import time
from kucoin.client import Margin, Market
from secrets import *
 
 
client = Margin(api_key, api_secret,passphrase)
#########################################
WAIT_TIME = 3
def extractActiveOrdersData(active_orders):
	currencies = []
	orderIds = []
	for i in active_orders:
		currency = get_currency(i)
		if(currency not in currencies):
			currencies.append(currency)
		orderIds.append(getOrderId(i))
	return currencies, orderIds

def get_currency(active_order):
	return active_order['currency']

def getOrderId(active_order):
	return active_order['orderId']

def cancelOrders(orderIds):
	for i in orderIds:
		client.cancel_lend_order(i)

def autoLendCurrencies(currencies):
	for i in currencies:
		print(i)
		client.set_auto_lend(i,False, retainSize = 0, dailyIntRate= 0, term = 7)
		time.sleep(WAIT_TIME)
		client.set_auto_lend(i,True, retainSize = 0, dailyIntRate= 0, term = 7)
		time.sleep(WAIT_TIME)


activeOrders = client.get_active_order()
print(activeOrders['items'])
(currencies, orderIds) = extractActiveOrdersData(activeOrders['items'])
cancelOrders(orderIds)
autoLendCurrencies(currencies)
print("Hacido")
