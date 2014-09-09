# Even though you'll create two bicycle manufacturers, assume that all manufacturers use the same three wheel types.
# Even though you'll create two bicycle manufacturers, assume that all manufacturers use the same three frame types.

class Wheels():
  def __init__(self, wheelWeight, wheelName, wheelCost):
    self.wheelWeight = wheelWeight         # Have a weight
    self.wheelName = wheelName             # Have a model name
    self.wheelCost = wheelCost             # Have a cost for manufacturer to produce

class Frames():
  def __init__(self, frameMaterial, frameCost, frameWeight):
    self.frameMaterial = frameMaterial     # Can be made of aluminunum, carbon, or steel
    self.frameCost = frameCost             # Have a cost for manufacturer to produce
    self.frameWeight = frameWeight         # Have a weight


small = Wheels(10, "Tiny", 75.00)
medium = Wheels(20, "Mid-sized", 150.00)
large = Wheels(30, "Big-uns", 300.00)

print small.wheelWeight, small.wheelName, small.wheelCost
print medium.wheelWeight, medium.wheelName, medium.wheelCost
print large.wheelWeight, large.wheelName, large.wheelCost
