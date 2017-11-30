import unittest
import profit

"""
Test class for stock profit module

Author: Tony Myers
Date: 11/29/2017
"""
class TestStringMethods(unittest.TestCase):

	# stock keeps going up
	def testSkyrocket(self):
		self.assertEqual(profit.profit([1,2,5]), 4)

	# proft highest in first half of day, no new lows after
	def testProfitHighestFirstHalfNoNewLowsAfter(self):
		self.assertEqual(profit.profit([2,2,5,5,3,4]), 3)
	
	# proft highest in first half of day, new lows after
	def testProfitHighestFirstHalfNewLowsAfter(self):
		self.assertEqual(profit.profit([2,2,5,5,1,2,3]), 3)
		
	# proft highest in second half of day, no new high
	def testProfitHighestSecondHalfDayNoNewHigh(self):
		self.assertEqual(profit.profit([2,2,5,5,1,1,5]), 4)
		
	# proft highest in second half of day, new high
	def testProfitHighestSecondHalfDayNewHigh(self):
		self.assertEqual(profit.profit([2,2,5,5,1,1,7]), 6)
		
	# stock is tanking and never turns upwards
	def testTank(self):
		self.assertEqual(profit.profit([4,2,1]), -1)
		
	# stock flatlining
	def testFlatlining(self):
		self.assertEqual(profit.profit([4,4,4]), 0)
	
	# stock suspended from trading for the day
	def testSuspended(self):
		self.assertEqual(profit.profit([]), 0)

if __name__ == '__main__':
    unittest.main()