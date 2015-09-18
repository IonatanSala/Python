# takes a strings as a template with placeholder variables to be over written
# You then substitute the values in with a dictionary. The key being the placeholder name
# Placeholder names follow the same rules as varibles naming in python
# Template("$name is friends with $friend")

from string import Template

class MyTemplate(Template):
	delimiter = '#'



def Main():
	cart = []
	cart.append(
		{
			"item": "Coke",
			"price": 8,
			"qty": 2
		}
	)
	cart.append(
		{
			"item": "Cake",
			"price": 12,
			"qty": 1
		}
	)
	cart.append(
		{
			"item": "Fish",
			"price": 32,
			"qty": 4
		}
	)

	#t = Template("$qty x $item = $price")
	#total = 0;
	#print("Cart:")

	#for data in cart:
	#	print(t.substitute(data))
	#	total += data["price"]

	#print(total)

	t = MyTemplate("#qty x #item = #price")
	total = 0;
	print("Cart:")

	for data in cart:
		print(t.substitute(data))
		total += data["price"]

	print(total)




if __name__ == '__main__':
	Main()