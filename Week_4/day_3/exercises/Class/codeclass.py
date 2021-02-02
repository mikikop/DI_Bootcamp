person = {
	"name":"Jon", 
	"surname":"Spiller",
	"job": "Teacher",
	"pets": 3.5,
	"pet_names": ["Fluffy", "Jaws", "Robin"],
	"work_experience": {
		"programmer": "Nedcore",
		"teacher": "Developers Institute",
		"waiter": "Burger King"
	},
	"parents": ("Mom", "Dad"),
	99: "Red Balloons", 
	("A", "B"): "The alphabet" 
}
​
​
# keys can be any immutable object
​
shopping_dict = {
	0: "Apples",
	1: "Oranges",
	2: "Bananas"
}
​
# Dicts are not ordered!
​
shopping_list = ["Apples", "Oranges", "Bananas"]
​
​
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
​
​
​
​
inventory = {
	"apples": 100,
	"oranges": 500,
	"bananas": 200
}
​
# to access a dictionary value
inventory["apples"]
inventory.get("apples")
​
# to update a dictionary value
inventory["apples"] = 1000
​
​
# keys and values:
​
mykey = inventory.keys()
​
myvalues = inventory.values()
​
myitems = inventory.items() # list of tuples
​
​
​
countries = [
	(
		"Israel", 
		{
			"population":8000000,
			"location": "Middle East",
			"flag": ["blue", "white"]
		}
	), 
	(
		"South Africa", 
		{
			"population":65000000,
			"location": "Africa",
			"flag": ["blue", "white", "red", "green", "yellow", "black"]
		}
	), 
	(
		"USA", 
		{
			"population":350000000,
			"location": "North America",
			"flag": ["blue", "white", "red"]
		}
	), 
]
​
#Get the color green
mycolor = countries[1][1]['flag'][3]
​
​
​
inventory = {
	"apples": 100,
	"oranges": 500,
	"bananas": 200,
	"dogs": 2,
	"chicken": 60,
	"dollars": 0
}
​
# Loop through the dictionary and print:
# "I have <number> of <fruit>" for each line
#SOLUTION
for name, number in inventory.items():
	print(f"I have {number} of {name}")
​
​
# Other Options
​
fruits_list = inventory.items()
for fruit_item in fruits_list:  #fruit_item = ("apples", 100)
	print(f"I have {fruit_item[1]} of {fruit_item[0]}")
​
​
fruit_names = inventory.keys()    # ["apples", "oranges", "banana"]
for single_fruit in fruit_names:
	number = inventory[single_fruit]
	print(f"I have {number} of {single_fruit}")
​
​
​
# Generate a list of numbers from 1 to 1 million.
​
numbers = []
for i in range(1,1000001):
	numbers.append(i)
​
#LIST COMPREHENSION
​
numbers = [i for i in range(1,1000001)]
​
​
# MORE EXAMPLES
​
​
# generate a list of the first 10 squares
numbers = []
for i in range(1,11):
	numbers.append(i*i)
print(numbers)
​
numbers = [i*i for i in range(1,11)]
print(numbers)
​
​
# lets make a dictionary from 100 to 110 where the key is a number and the value is half of the number
​
# {
# 	100: 50
# 	101: 50.5
# 	102: 51
# 	...
# 	..
# 	110:55
# }
​
numbers = {}
for i in range(100,111):
	numbers[i] = i/2
print(numbers)
​
numbers = { i:i/2 for i in range(100,111)}
print(numbers)
​
​
​
# Ask 3 users for their names, put their names in a list...
​
names = []
for i in range(3):
	name = input("What is your name? ")
	names.append(name)
print(names)
​
names = [input("Enter your name: ") for i in range(3)]
print(names)
​
​
# generate a list of numbers between 1 and 100 if the number is divisble by 7
​
numbers = []
for i in range(1,101):
	if i % 7 == 0:
		numbers.append(i)
print(numbers)
​
​
numbers = [i if i % 7 == 0 else ":)" for i in range(1,101)]
print(numbers)
