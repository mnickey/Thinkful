class BikeShops(object):
	""" Bike Shops have a name, an inventory. 
	Bike shops also sell bikes for a profit and can report that profit.
	"""
	def __init__(self, shop_name, inventory_list, customer_list):
		self.shop_name = shop_name
		self.inventory_list = inventory_list
		self.customer_list = customer_list
		self.shop_balance = 0.00

	def sell_bike(self, cust):
		for bike in self.inventory_list:
			if cust.can_buy(bike):
				self.shop_balance += cust.buy_bike(bike)
				cust.own_bike(bike)
				bike.soldFlag = True
				print "{0} bought the {1} bike from {2}.".format(
					cust.cust_name, 
					bike.modelName,
					self.shop_name
				)
				return
		print "\nNo bikes can be bought by {0}.".format(cust.cust_name)
		return

	def report(self):
		print "\n"
		print "{0}".format(self.shop_name).center(70, '-')
		print "{0} current store balance: {1}".format(
			self.shop_name, 
			self.shop_balance)
		print "{0}".format(self.shop_name).center(70, '-')
		return

"""
*Primary*
Done -- A bike shop has an inventory
Done -- A bike shop has customers
Done -- A bike shop has a name
A bike shop sells bicycles with a margin over their cost
A bike shop has a bank balance
	*Secondary*
"""
