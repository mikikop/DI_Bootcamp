#Ex1

# def doc(function):
# 	"""print the doc of the function in parameter"""
# 	print(function.__doc__)


# doc(abs)
# doc(int)
# doc(input)

# doc(doc)



#Ex2

class Currency:
	
	def __init__(self, label, amount):
		self.amount = amount
		if self.amount > 1:
			self.label = label + "s"
		else:
			self.label = label
		
	def __str__(self):
			return str(self.amount) + " " + self.label

	def __int__(self):
		return self.amount

	def __repr__(self):
		return str(self.amount) + " " + self.label

	def __add__(self,other):
		if isinstance(other, int):
			return Currency(self.label, self.amount + other)
		elif isinstance(other, Currency):
			if self.label == other.label:
				return Currency(self.label, self.amount + other.amount)	
			else:
		 		raise TypeError(f"Cannot add between Currency type {self.label} and {other.label}")

	def __iadd__(self,other):
		if isinstance(other, int):
			 self.amount += other
			 return self
		elif isinstance(other, Currency):
			if self.label == other.label:
				self.amount += other.amount
				return self
			else:
		 		raise TypeError(f"Cannot add between Currency type {self.label} and {other.label}")

	

# if __name__ == "__main__":
# 	c1 = Currency('dollar', 5)
# 	c2 = Currency('dollar', 10)
# 	c4 = Currency('shekel', 1)
# 	c3 = Currency('shekel', 10)
