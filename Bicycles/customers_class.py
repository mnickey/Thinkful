class Customers(object):
	"""docstring for Customers"""
	def __init__(self, cust_name, cust_funds):
		super(Customers, self).__init__()
		self.cust_name = cust_name
		self.cust_funds = cust_funds
		self.garage = []

	# Method to see if the customer can buy a bike
	def can_buy(self, bike):
		""" Returns true if the customers funds are greater than or equal to the bikes shop cost. """
		return (self.cust_funds >= bike.shopCost)

	def buy_bike(self, bike):
		self.cust_funds -= bike.shopCost
		return bike.shopCost 

	def own_bike(self, bike):
		self.garage.append(bike)
		self.buy_bike(bike)
		return bike.shopCost

"""
*Primary*
Done -- A customer has a name
Done -- A customer has a bank balance
A customer can buy a bike
A customer can own a bike (stored in a garage)
	*Secondary*
"""