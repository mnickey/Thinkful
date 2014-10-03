# creating a Bicycle class
class Bicycle(object):
	""" Object class for Bicycle's. Has a model name, a weight and a cost to produce. """
	def __init__(self, modelName, weight, prodCost):
		self.modelName = modelName
		self.weight = weight
		self.prodCost = prodCost
		self.shopCost = prodCost * 1.20
		self.soldFlag = False


