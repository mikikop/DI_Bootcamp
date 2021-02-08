from cprint import cprint
class Person:   #Super Class
	def __init__(self, name, age):
		cprint.err("In the INIT of PERSON class")
		self.name = name
		self.age = age
		cprint.err("finishing INIT of PERSON class")
	def info(self):
		print(f"{self.name} is {self.age} years old")
	def birthday(self):
		self.age += 1
		print("Happy Birthday!")
		
class Man(Person):  #Sub Class
	def __init__(self, name, age, favorite_beer):
		cprint.info("In the INIT of MAN class")
		super().__init__(name, age)
		self.favorite_beer = favorite_beer
		self.gender = "Male"
		cprint.info("Finishing INIT of MAN class")
	def birthday(self):
		super().birthday()
		print("Lets get beers!")
	def drink_beer(self):
		print("Glug glug glug")
# Inheritance
# -----------
# class SubClass(SuperClass)
# We can add new methods
# We can override parent/super methods
# We can call parent class with super()



class Account:
	def __init__(self, acc_number):
		self.acc_number = acc_number
		self.__balance = 0
		self.__transaction_history = []
	def deposit(self, amount):
		if amount > 0 and amount <= 10000:
			self.__balance += amount
		self.__transaction_history.append(f"Deposit: {amount}")
	def withdraw(self, amount):	
		if amount <= self.__balance:
			self.__balance -= amount
			self.__transaction_history.append(f"Withdraw: {amount}")
			return amount
		else:
			print("Insufficient Funds!")
	def info(self):
		print(f"Account {self.acc_number} has balance ${self.__balance}.")
	def transaction_history(self):
		for transaction in self.__transaction_history:
			print(transaction)


# OTHER LANGUAGES HAVE:
# public = Accessible Anywhere
# protected = Accessible in the class and in all subclasses
# private = Accessible only in the current class
# PYTHON HAS:
# _  single underscore (indication to other programmers that this should "ACT" like protected. 
#		But actually does nothing)
# __ double underscore (acts like private, and cannot be accessed outside the class)


animals = ["dog", "cat"]
user_input = input("Which animal (number) do you want? ")
try:
	index = int(user_input)
	print(animals[index])
except ValueError:
	print("Your input must be a number")
except IndexError:
	print(f"Number must be between 0 and {len(animals)}")
except Exception:
	pass #catch all other exceptions
finally:
	print("We are done.")

#Using exception  handling to add numbers in a list, 
#even when the list contains garbage information:

mylist = [2,3,1,"four",2,42,1,5,3,None]
def make_sum(mylist):
	total = 0
	for num in mylist:
		try:
			total += num
		except TypeError:
			continue
	return total
total = make_sum(mylist)
print(total)