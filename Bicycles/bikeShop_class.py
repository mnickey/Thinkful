class BikeShops(object):
	""" Bike Shops have a name, an inventory. 
	Bike shops also sell bikes for a profit and can report that profit.
	"""
	def __init__(self, shop_name, shop_inventory, shop_markup):
		self.shop_name = shop_name
		self.shop_inventory = shop_inventory
		self.shop_markup = shop_markup