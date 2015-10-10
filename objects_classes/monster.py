# our monster class
import random

COLORS = ["yellow", "red", "blue", "green"]
class Monster:

	min_hit_points = 1
	max_hit_points = 1
	min_experience = 1
	max_experience = 1
	weapon = "sword"
	sound = "Roar"

	def __init__(self, **kwargs):
		#self.name = kwargs.get('name', "Monster")
		#self.hit_points = kwargs.get('hit_points', 1)
		#self.color = kwargs.get('color', "yellow")
		#self.weapon = kwargs.get('weapon', "sword")
		#self.sound = kwargs.get('sound', "Roar!")

		self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
		self.experience = random.randint(self.min_experience, self.max_experience)
		self.color = random.choice(COLORS)

		for key, value in kwargs.items():
			setattr(self, key, value)

	def present_yourself(self):
		print("Hi, my name is " + self.name)
		print("I have " + self.weapon + " and I'm " + self.color)


