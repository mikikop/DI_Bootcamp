Inheritance
  IS A TYPE OF
Composition
  HAS ONE OR MORE OF
class Person:
	def __init__(self, name, age, language):
class Language:
	def __init__(self, name, region, first_spoken_date):
class Superman(Person):
	def __init__(self, name, age, super_powers, planet)
lang = Language("English", "UK", "850BC")
p1 = Person("bob", 1, Language("Greek", "France", "2021"))
# SUPERMAN IS A PERSON: Therefore Superman inherits from Person
# SUPERMAN HAS A LANGUAGE
# PERSON HAS A LANGUAGE
# So Person is composed of a Language


# Dunder
# Double Under
# Methods that start and end with 2 underscores
# Dunder methods are exactly like normal methods / function
# Except. They run automatically under certain circumstances...
# __repr__   show a string representation of the class
# it runs wheneve a variable is dumped in the terminal


# __init__:  Called when an object is instantiated.
# __repr__:  Called when you dump an object variable on screen
# __str__: Called when you print a variable
# str is more informal than repr
# > calls __gt__
# + calls __add__



#Classmethods, Staticmethods, Properties

class Circle:
	PI = 3.14159265
	count = 0
	def __init__(self, radius):
		self.radius = radius
		Circle.count += 1
	@property   # GETTER (You can also look up SETTER)
	def area(self):
		return Circle.PI * self.radius**2
	def circumference(self, radius):
		return Circle.PI * self.radius*2
	@classmethod
	def getpi(cls):
		return cls.PI
	@staticmethod
	def info(how_many_times):
		for i in range(how_many_times):
			print("A circle is a shape consisting of all points in a plane that are a given distance from a given point, the centre")



#From the Terminal.
# ~ pip --version
# If you have pip installed you will see the version number.
# ~ pip install cprint
# This will download and install the cprint package

from cprint import cprint  #import the package / module
cprint.ok("This will print in blue")
cprint.info("This will print in green")
cprint.warn("This will print in orange")
cprint.err("This will print in red")

#sys module

import sys
if __name__ == "__main__":
# if this file was loaded from the terminal
	total = 0
	for num in sys.argv[1:]:
		total += int(num)
	print(total)


#clock

from time import sleep
from cprint import cprint  # IF YOU DONT HAVE CPRINT INSTALLED. USE NORMAL PRINT
from datetime import datetime
while True:
	x = datetime.now()
	cprint.info(x.strftime("%H:%M:%S"))
	sleep(1)