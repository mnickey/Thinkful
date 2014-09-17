# BikePart - parent class for frame and wheels
class BikePart(object):
	def __init__(self, cost, weight):
		self._cost = cost
		self._weight = weight

class Wheel(BikePart):
	"""Creates a wheel with name, cost and & weight. Uses an instance of the BikePart object to do so."""
	def __init__(self, name, cost, weight):
		super(Wheel, self).__init__(cost, weight)
		self._name = name

# Create three wheel types
class RoadBike(Wheel):
	pass
class MountainBike(Wheel):
	pass
class MotorBike(Wheel):
	pass

class Frame(BikePart):
	"""Creates a frame with name, cost and & weight. Uses an nstance of the BikePart object to do so."""
	def __init__(self, name, cost, weight):
		super(Frame, self).__init__(cost, weight)
		self._name = name

# Create three frame types -- aluminunum, carbon & steel
class Aluminunum(Frame):
	pass
class Carbon(Frame):
	pass
class Steel(Frame):
	pass

class Material(object):
	ALUMINUM = "Aluminum"
	CARBON= "Carbon"
	STEEL = "Steel"

"""
Comprised (in our simplified world) of two wheels of the same type and a frame.
Have a total weight equal to the sum of the weight of the frame and two wheels.
Have a total cost to produce (for our purposes, that cost is the sum of the two wheels' and frame's cost to produce)
Have a name
Have a manufactuer
"""
# Models have two wheels, a frame, a cost, a name and a manufacturer
class Model(self):
	def __init__(self, frame, frontWheel, backWheel):
		self.frame = frame
		self.frontWheel = frontWheel
		self.backWheel = backWheel

class ModelA(Model):
	super(Model, self).__init__(self, frame, frontWheel, backWheel)
	self.name = "Model A"

class ModelB(Model):
    super(Model, self).__init__(self, frame, frontWheel, backWheel)
	self.name = "Model B"

class ModelC(Model):
    super(Model, self).__init__(self, frame, frontWheel, backWheel)
	self.name = "Model C"

"""
Create two bicycle manufacturers, assume that all manufacturers use the same three frame types.
Have a name, produce three models of bikes each, have a percentage over cost they sell to bike shops at
I created one manufacter class that can create multiple manufacturer objects
"""
class BikeManufacturer(object):
	def __init__(self, name, model, percentage):
		self._name = name
		self._percentage = .25
		self.model = ["modelA", "asd2", "asd"]

class Huffy(BikeManufacturer):
	super(BikeManufacturer, self).__init__(self, name, model, percentage)

class Trek(BikeManufacturer):
	super(BikeManufacturer, self).__init__(self, name, model, percentage)

"""
Bike Shops:
Get their inventory of bikes from manufacturers
Sell bicycle models with a margin over price they pay to manufacturer
Have a name
Have an inventory
Can see how much profit they have made on margin from selling bikes.
"""
class BikeShop(object):
	def __init__(self, inventory, name, margin):
		self.inventory = inventory
		self.name = name
		self.margin = .25

"""
Customers: Have a name, Have a fund of money to buy a bike, Can buy and own a new bicycle
"""
class Customers(object):
	"""Customers: Have a name, Have a fund of money to buy a bike, Can buy and own a new bicycle"""
	def __init__(self, name, funds, ownership):
		super(Customers, self).__init__()
		self.name = name
		self.funds = funds
		self.ownership = ownership

"""Test print items. Can be deleted or commented out when the class is complete."""
small_wheel = Wheel("super small wheel", 10, 100)
print "Your wheel is {0} and it costs {1} and it weighs {2}.".format(small_wheel._name, small_wheel._cost, small_wheel._weight)
small_frame = Frame("tiny", 13, 17)
print "Your frame is {0}, it costs {1} and weighs {2}.".format(small_frame._name, small_frame._cost, small_frame._weight)
myManu = BikeManufacturer("Mikes Bikes", "Bad Bikes", .20)
print "Your Bike manufacturer's name: {0}, Mark-up percentage: {1}.".format(myManu._name, myManu._percentage)

# Notes:
# source venv/bin/activate
# virtualenv venv