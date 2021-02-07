import math
import random

#Ex1
# class Circle:
# 	"""docstring for Circle"""
# 	def __init__(self, radius=1.0):
# 		super(Circle, self).__init__()
# 		self.radius = radius

# 	def perimeter(self):
# 		return 2*math.pi*self.radius

# 	def area(self):
# 		return math.pi*(self.radius)**2

# 	def geo_def(self):
# 		print(f"The perimeter of the circle is {self.perimeter()}")
# 		print(f"The area of the circle is {self.area()}")


# circle1 = Circle(5)
# circle1.geo_def()

#Ex2
class MyList:
	"""docstring for MyList"""
	def __init__(self, my_list):
		super(MyList, self).__init__()
		self.my_list = my_list

	def reversed_list(self):
		return self.my_list.reverse()

	def sorted_liste(self):
		return self.my_list.sorted()

	def list_gen(self):
		return [random.randint(0,100) for x in self.my_list]



