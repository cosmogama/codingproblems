"""
Stock algorithm to pick the best time period within yesterdays trading range to buy and then sell the stock to maximize proft.

Source:
https://www.interviewcake.com/question/java/stock-price

Author: Tony Myers
Date: 11/29/2017
"""
import sys

MIN = sys.maxsize * -1
MAX = sys.maxsize

def profit(prices):
	print("Calculating profit for prices [" + ",".join(map(str,prices)) + "]")
	if(len(prices) == 0):
		print("Profit=0")
		return 0
	lowest = MAX
	highest = MIN
	maxprofit = MIN
	for i, price in enumerate(prices):
		if(price < lowest):
			# record the new max profit
			if(highest > MIN and lowest < MAX):
				if(maxprofit < highest - lowest):
					maxprofit = highest - lowest
			# case where stock is dropping to new lows consecutively (will produce negative profit)
			elif(lowest < MAX):
				if(maxprofit < price - lowest):
					maxprofit = price - lowest
			# reset lowest
			lowest = price
			# reset highest because it must come after the new lowest point
			highest = MIN
		elif(price > highest):
			highest = price
			if(maxprofit < highest - lowest):
				maxprofit = highest - lowest
		# print("DEBUG: {0} P={1} L={2} H={3} M={4}".format(i, price, lowest, highest, maxprofit))
	print("Profit={0:d}".format(maxprofit))
	return maxprofit
	

