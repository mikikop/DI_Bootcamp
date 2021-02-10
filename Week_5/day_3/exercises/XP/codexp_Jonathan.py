from print import print

class Currency:

	def __init__(self, label, amount):
		self.label = label
		self.amount = amount

	def __repr__(self):
		return f"{self.amount} {self.label}"

	def __add__(self, other):
		if isinstance(other, int):
			return Currency(self.label, self.amount + other)
		if self.label != other.label:
			raise CurrecyMismatch("Currency types must be the same")
		return Currency(self.label, self.amount + other.amount)

class CurrecyMismatch(Exception):

	def __init__(self, message):
		super().__init__(self)
		self.message = message
		print.err(message)




c1 = Currency("dollar", 5)
c2 = Currency("dollar", 2)
c3 = Currency("euro", 4)














