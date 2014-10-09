from bicycle_class import Bicycle
from bikeShop_class import BikeShops
from customers_class import Customers
# from bicycle_class import Bicycle, BikeShops, Customers

if __name__ == '__main__':
	""" Create 6 different bicycle models based on the imported Bicycle class """
	# Creating 6 different bikes
	bike1 = Bicycle("Roadster", 25, 150.00)
	bike2 = Bicycle("Mountaineer", 50, 160)
	bike3 = Bicycle("Horizontal Hipster", 75, 400)
	bike4 = Bicycle("Speedster", 25, 290)
	bike5 = Bicycle("Trail Blazer", 45, 425)
	bike6 = Bicycle("Single Forever Sitdowner", 65, 650)
	# Adding bikes to the manufacturers inventory
	inventory_list = [bike1, bike2, bike3, bike4, bike5, bike6]

	# Creating 3 different customers
	mike = Customers("Mike", 1000)
	charles = Customers("Charles", 500)
	christine = Customers("Christine", 200)
	# Adding customers to customer list.
	customer_list = [mike, christine, charles]
	
	#Creating a bike shop
	print '\n'
	myStore = BikeShops("Mike's Bikes", inventory_list, customer_list)
	myStore.sell_bike(mike)
	myStore.sell_bike(charles)
	myStore.sell_bike(christine)
	myStore.report()
