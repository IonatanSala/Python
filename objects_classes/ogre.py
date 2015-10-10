# import my Monster class from monster.py
from monster import Monster

def main():

	#ogre = Monster(name="Ogre", color="green", weapon="Machine Gun", hit_points=10, sound="Argh! I'm going to eat you!")
	#ogre.present_yourself();

	ogre = Monster(name="Marty the Ogre", color="green", weapon="Light Saber")

	ogre.present_yourself()


if __name__ == "__main__":
	main()