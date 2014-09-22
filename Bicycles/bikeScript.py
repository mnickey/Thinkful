"""
Tasks (grouped):
Done -- Import your classes from a separate file.
Done -- Create a bicycle shop that has 6 different bicycle models in stock. -- Inefficient but done.
In Progress -- The shop should charge its customers 20% over the cost of the bikes. 

In Progress -- Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
In Progress -- Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.

In Progress -- Print the initial inventory of the bike shop for each bike it carries.

In Progress -- Have each of the three customers purchase a bike. 
In Progress -- Then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
In Progress -- After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, 
	and how much profit they have made selling the three bikes.
"""

from bicycle_class import Bicycle, BikeShops, Customers

nameList = ["Road Bike", "Mountain Bike", "Reclining Bike"]
costList = [150, 175, 200]
weightList = [25, 50, 75]

bikeTup = ("Road Bike", "Roadster", "Weight", 25, "Cost", 150)
shopDict = {}

	# for x in range(3):
	# 	temp = Bicycle(nameList[x], costList[x], weightList[x])
	# 	print temp
	# shopDict.add(huffy)
	# return shopDict



if __name__ == '__main__':
	""" Create 6 different bicycle models based on the imported Bicycle class """
	huffy = Bicycle("Roadster", 25, 150.00)
	huffyShopCost = huffy.prodCost * 1.20
	
	huffy2 = Bicycle("Mountaineer", 50, 200)
	huffy2ShopCost = huffy2.prodCost * 1.20 

	huffy3 = Bicycle("Horizontal Hipster", 75, 400)
	huffy3ShopCost = huffy3.prodCost * 1.20 
	
	trek = Bicycle("Speedster", 20, 275)
	trekShopCost = trek.prodCost * 1.20 

	trek2 = Bicycle("Trail Blazer", 45, 425)
	trek2ShopCost = trek2.prodCost * 1.20 

	trek3 = Bicycle("Single Forever Sitdowner", 65, 650)
	trek3ShopCost = trek3.prodCost * 1.20 	

	print huffy.modelName, huffy.weight, huffy.prodCost, huffyShopCost
	print huffy2.modelName, huffy2.weight, huffy2.prodCost, huffy2ShopCost
	print huffy3.modelName, huffy3.weight, huffy3.prodCost, huffy3ShopCost
	print trek.modelName, trek.weight, trek.prodCost, trekShopCost
	print trek2.modelName, trek2.weight, trek2.prodCost, trek2ShopCost
	print trek3.modelName, trek3.weight, trek3.prodCost, trek3ShopCost