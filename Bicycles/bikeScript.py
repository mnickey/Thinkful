"""
Tasks (grouped):
Done -- Import your classes from a separate file.
Done -- Create a bicycle shop that has 6 different bicycle models in stock. -- Inefficient but done.
Done -- The shop should charge its customers 20% over the cost of the bikes. -- Inefficient but done.

Done -- Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
Done -- Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. 

Done -- Print the initial inventory of the bike shop for each bike it carries.

In Progress -- Have each of the three customers purchase a bike. 
In Progress -- Then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
In Progress -- After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, 
	and how much profit they have made selling the three bikes.
"""

from bicycle_class import Bicycle, BikeShops, Customers

if __name__ == '__main__':
	""" Create 6 different bicycle models based on the imported Bicycle class """
	inventory_list = []
	inventory_list = [Bicycle("Roadster", 25, 150.00), \
	Bicycle("Mountaineer", 50, 200), \
	Bicycle("Horizontal Hipster", 75, 400), \
	Bicycle("Speedster", 25, 290), \
	Bicycle("Trail Blazer", 45, 425), \
	Bicycle("Single Forever Sitdowner", 65, 650)]
	
	print "Inventory"
	print "-" * 20
	for i in range(len(inventory_list)):
		print inventory_list[i].modelName, inventory_list[i].weight, \
		inventory_list[i].prodCost, inventory_list[i].shopCost
	
	""" Create three customers. One customer has a budget of $200, the second $500, and the third $1000 """
	customer_list = []
	customer_list = [Customers("Michael", 500.0), \
	Customers("Charles", 1000), \
	Customers("Christine", 200)]
	print '\nCustomers'
	print '-' * 20
	for i in range(len(customer_list)):
		print "{0} has {1} dollars for a new bike.".format(customer_list[i].cust_name, customer_list[i].cust_funds)

	print '\nCustomers'
	for i in range(len(customer_list)):
		print '-' * 20
		for x in range(len(inventory_list)):
			if inventory_list[x].prodCost < customer_list[i].cust_funds:
				print "{0} can afford the {1}".format(customer_list[i].cust_name, inventory_list[x].modelName)
	print '-' * 20