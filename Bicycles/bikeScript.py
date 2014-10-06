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
	myStore = BikeShops("Mike's Bikes", inventory_list, customer_list)
	print myStore.inventory_list[0].modelName





	# Bicycle.print_inventory(inventory_list)
	
	# # Not using the BikeShops class -- need to implement and add into a shop using the BikeShop class
	# print "Inventory"
	# print "-" * 20
	# for i in inventory_list:
	# 	print i.modelName, i.weight, i.prodCost, i.shopCost
	
	# """ Create three customers. One customer has a budget of $200, the second $500, and the third $1000 """
	# customer_list = []
	# customer_list = [Customers("Michael", 500.0), \
	# Customers("Charles", 1000), \
	# Customers("Christine", 200)]
	# print '\nCustomers'
	# print '-' * 20
	# for i in customer_list:
	# 	print "{0} has {1} dollars for a new bike.".format(i.cust_name, i.cust_funds)

	# print '\nCustomers'
	# for i in customer_list:
	# 	print '-' * 20
	# 	for x in inventory_list:
	# 		if x.prodCost < i.cust_funds:
	# 			print "{0} can afford the {1}".format(i.cust_name, x.modelName)
	# print '-' * 20

	# print '\nPurchasing'
	# print '-' * 20
	# for i in customer_list:
	# 	for b in inventory_list:
	# 		if b.shopCost <= i.cust_funds:
	# 			print "{0} ---- {1} --- {2}".format(i.cust_name, b.modelName, b.shopCost)

	# print '\nPurchasing'
	# print '-' * 20
	# for cust in customer_list:
	#     for item in inventory_list:
	#         if item.shopCost <= cust.cust_funds and item.soldFlag == False:
	#             item.soldFlag = True
	#             cust.cust_funds -= item.shopCost
	#             print "{0} has purchased {1} bike.".format(cust.cust_name, item.modelName)
                # inventory_list.remove(item)
	            # continue -- redundant

				# --- Pseudo Code ---
				# find the first item that the customer can purchase and buy it -- conditional if statement
				# if inventory_list[b].shopCost <= customer_list[i].cust_funds and inventory_list[b].soldFlag is False:
				
				# remove the funds from the customer -- these have to be done before removing the object from the list
				# add the funds to the bike shop -- these have to be done before removing the object from the list

				# remove the purchased bike from the inventor list -- del inventory_list[b]
				# inventory_list.remove(inventory_list[b])

				# instead of removing the bicycle from the list, set a flag in the class
				
				# re-loop over the bike inventory for the next customer
				# remove the print statement above

