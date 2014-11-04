import unittest
from discount_calc import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
    def testProperDiscount(self):
        discounted_total = calculate_discount(200, 10, 30)
        self.assertEqual(discounted_total, 150)

    def testZeroItemCost(self):
    	discounted_total = calculate_discount(0, 10, 30)
    	self.assertEqual(discounted_total, 0)

    def testItemCostBelowZero(self):
    	discounted_total = calculate_discount(-5, 10, 30)
    	self.assertEqual(discounted_total, 0)

    def testDiscountedTotalBelowZero(self):
    	discounted_total = calculate_discount(5, 10, 30)
    	self.assertEqual(discounted_total, 0)

    def testNegativeDiscount(self):
    	self.assertEqual(200, calculate_discount(200, -25, 0))
    	self.assertEqual(200, calculate_discount(200, 0, -25))

if __name__ == '__main__':
	unittest.main()