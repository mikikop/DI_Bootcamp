
class Farm:
	def __init__(self, name):
		self.name = name
		self.animals = {}
	def add_animal(self, name, amount=1):
		if name in self.animals:
			self.animals[name] += amount
		else:
			self.animals[name] = amount
	def get_info(self):
		print(f"{self.name}'s Farm\n")
		for name, amount in self.animals.items():
			print(f"{name} : {amount}")
		print("\n\tE-I-E-I-O")