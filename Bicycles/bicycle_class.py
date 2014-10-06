# creating a Bicycle class
class Bicycle(object):
	""" Object class for Bicycle's. Has a model name, a weight and a cost to produce. """
	
	def __init__(self, modelName, weight, prodCost):
		self.modelName = modelName
		self.weight = weight
		self.prodCost = prodCost
		self.shopCost = prodCost * 1.20
		self.soldFlag = False # A false flag denotes that the bike has not been sold.
		self.inventory_list = []

"""
*Primary*
Done -- A bicycle has a name
Done -- A bicycle has a weight
Done -- A bicycle has a cost to produce
	*Secondary*
	A bicycle is an object
	A bicycle has a frame
	A bicycle has two wheels
"""