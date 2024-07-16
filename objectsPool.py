import math

# all objects will be held here 

# make the pool ball class this will include:
'''
- position - tuple wiht x and y [x,y]
- velocity - tuple with x and y vectors. [x,y]
- radius - constent
- color/type - incremented 
- mass - constent
- friction - constent
- gravity - constent

with velocity will be the same untill a colition occers with wall or ball and we work out real time PE/KE taken.

also will include getter and methods to canculate:
- distance to another object
- collision
- movement
- draw

'''

# the color type is a string in HEX for pygame this is one way to do it.

class ball:
	def __init__(self, position: tuple[float,float], colorType: str, velocity: tuple[float, float]) -> None:
		self.position = position
		self.velocity = velocity
		self.colorType: str = colorType
		self.radius: float = 10
		self.mass: float = 1
		self.friction: float  = 0.1
		self.gravity: float = 0.1
	# getter methods
	def getPosition(self):
		return tuple([int(self.position[0]), int(self.position[1])]) 
		
	def getVelocity(self):
		return self.velocity
		
	def getColorType(self):
		return self.colorType
		
	def getRadius(self):
		return self.radius
		
	def getMass(self):
		return self.mass
		
	def getFriction(self):
		return self.friction
		
	def getGravity(self):
		return self.gravity
		
	# setter methods
	def setPosition(self, position):
		self.position = position
		
	def setVelocity(self, velocity):
		self.velocity = velocity
		
	# methods
	def distanceTo(self, other):
		return math.sqrt((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2)

	def collision(self, other): # will colition happen to balls 
		if self.distanceTo(other) <= self.radius + other.radius: # if the distance is less than the radius of the balls then ther is a collision.
			return True
		else:
			return False
			
	def movement(self):
		self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])