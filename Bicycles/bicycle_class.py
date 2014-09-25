# creating a Bicycle class
class Bicycle(object):
	""" Object class for Bicycle's. Has a model name, a weight and a cost to produce. """
	def __init__(self, modelName, weight, prodCost):
		self.modelName = modelName
		self.weight = weight
		self.prodCost = prodCost
		self.shopCost = prodCost * 1.20

class BikeShops(object):
	""" Bike Shops have a name, an inventory. 
	Bike shops also sell bikes for a profit and can report that profit.
	"""
	def __init__(self, shop_name, shop_inventory, shop_markup):
		self.shop_name = shop_name
		self.shop_inventory = shop_inventory
		self.shop_markup = shop_markup

class Customers(object):
	"""docstring for Customers"""
	def __init__(self, cust_name, cust_funds):
		super(Customers, self).__init__()
		self.cust_name = cust_name
		self.cust_funds = cust_funds
		
"""
The Scenario
For this project, we'll imagine that you've been hired by a business analyst to build a system that models the bicycle industry. 
You need to be able to model bicycles, which have a fixed cost to produce, 
bike shops, which sell bicycles with an added margin on top, 
and customers, who have different budgets for buying a bicycle.

Basic Requirements
Design Python classes
You should create classes to represent each of the following parts of our model:

Bicycle
	Have a model name
	Have a weight
	Have a cost to produce

Bike Shops
	Have a name
	Have an inventory of different bicycles
	Sell bicycles with a margin over their cost
	Can see how much profit they have made from selling bikes

Customers
	Have a name
	Have a fund of money to buy a bike
	Can buy and own a new bicycle

Write a script to test your classes
The script should:
	Import your classes from a separate file.
	Create a bicycle shop that has 6 different bicycle models in stock. 
	The shop should charge its customers 20% over the cost of the bikes.
	Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
	Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. 
	Make sure you price the bikes in such a way that each customer can afford at least one.

	Print the initial inventory of the bike shop for each bike it carries.
	Have each of the three customers purchase a bike then print the name of the bike the customer purchased, 
		the cost, and how much money they have left over in their bicycle fund.
	After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, 
		and how much profit they have made selling the three bikes.
"""