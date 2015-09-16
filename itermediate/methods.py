# Methods with classes in python3
import math

class Vector2D:

	# we dont need these attributes at the top here anymore 
	# because our __init__() will create them
	#x = 0.0
	#y = 0.0

	# always have to pass in self as a parameter
	#def Set(self,x, y):
	#	self.x = x
	#	self.y = y

	# adding __init__()
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self,other):
		return Vector2D(self.x + other.x, self.y + other.y)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self

	def __sub__(self, other):
		return Vector2D(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return Vector2D(self.x * other.x, self.y * other.y)

	def __imul__(self, other):
		self.x *= other.x
		self.y *= other.y

	def __truediv__(self, other):
		return Vector2D(self.x / other.x, self.y/other.y)

	def getLength(self):
		return math.sqrt(self.x**2 + self.y**2)

	def normalized(self):
		length = self.getLength()
		if length != 0:
			return Vector2D(self.x/length, self.y/length)
		return Vector2D(self)

	def getAngle(self):
		return math.degrees(math.atan2(self.y,self.x))

	def __str__(self):
		return "X: " + str(self.x) + ", Y: " + str(self.y)

def Main():
	vec = Vector2D(5,10)
	vec2 = Vector2D(2, 4)
	# We don't have to set self because python know that that is referring to that class
	# and we don't have to pass it in
	#vec.Set(5,10)
	print(vec)
	print(vec2)

	vec = vec + vec2
	
	print(vec)


if __name__ == '__main__':
	Main()