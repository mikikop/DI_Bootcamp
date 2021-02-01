#Ex1
# my_fav_numbers = {2,4,6,7}
# my_fav_numbers.add(9)
# my_fav_numbers.add(11)
# my_fav_numbers.remove(11)
# print(my_fav_numbers)
# friend_fav_numbers = {1,2,3,4}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#Ex2
#A tuple is immutable. it's not possible to add and change anything inside a tuple

#Ex3
# for x in range(1,21):
# 	print(x)

#Ex4
#float is a number with decimal point. integer has not decimal point
# list_x = []
# list_y = []
# list_f = []

# for x in range(1,6):
# 	x=x+0.5
# 	y = int(x + 0.5)
# 	list_y.append(y)
# 	list_x.append(x)
# 	list_f = (list_x + list_y)
# list_f.sort()
# list_f.remove(6.0)
# list_f.remove(5.5)
# print(list_f)


# list_new = []
# for x in range(3,11):
# 	num = x/2 if x%2 == 1 else int(x/2)
# 	list_new.append(num)
# print(list_new)

# list_new2=[x/2 if x%2 == 1 else int(x/2) for x in range(3,11)]
# print(list_new2)


#Ex5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")
# basket.pop(len(basket)-1)
# basket.append("kiwi")
# basket.insert(0,"Apples")
# basket.count("Apples")
# basket.clear()
# print(basket)


# Ex6
# name = ''
# while name != "mike":
# 	name = input("Enter names until you guess mine: ")


#Ex7
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# x=0
# while x != len(basket) :
# 	print(basket[x])
# 	x=x+2
	
#Ex8
# list_mult=[]
# for x in range(3,31):
# 	if x%3 == 0:
# 		list_mult.append(x)
# print(list_mult)

#Ex9
# list_mult=[]
# for x in range(1500,2701):
# 	if x%5 == 0 and x%7 == 0:
# 		list_mult.append(x)
# print(list_mult)

#Ex10
# answer = input("Please enter your favorite fruits separated by space: ")
# my_fav_fruits = answer.split(" ")
# answer2 = input("Please enter one of your favorite fruits: ")
# if answer2 in my_fav_fruits:
# 	print("You chose one of your favorite fruits! Enjoy!")
# else:
# 	print("You chose a new fruit. I hope you enjoy it too!")

# my_string=""
# for x in my_fav_fruits:
# 	if x != my_fav_fruits[-1]:
# 		my_string = my_string + " " + x
# 	else:
# 		my_string = my_string + " and " + x 
# print(" The list of fruits is : " + my_string)


#Ex11
# answer = ""
# list_toppings = []

# while answer != "quit":
# 	answer = input("Enter pizza toppings you want (to quit just enter quit): ")
# 	list_toppings.append(answer)
# 	if answer  == "quit":
# 		break
# 	print("We've just added " + answer + " to your toppings list")

# list_toppings.pop(-1)
# total = 10 + (2.5*len(list_toppings))
# print ("Your pizza will contain the following topppings:", *list_toppings, "and the price will be", total,"₪")


#Ex12
# answer = input("How many people are you in the family? ")
# family = int(answer)
# list_age = []
# total = 0

# for x in range(1,family+1):
# 	answer2 = input("What is the age of the first person? ")
# 	age = int(answer2)
# 	list_age.append(age)

# for x in list_age:
# 	if x>=12:
# 		total = total + 15
# 	elif x>3 and x<12:
# 		total = total + 10
# 	else:
# 		total = total + 0

# print("The total cost for your family is: ",total)

#Ex12 question 4
# answer = input("How many people are you in the group? ")
# group = int(answer)
# list_age = []
# list_allowed = []
# list_name = []

# for x in range(1,group+1):
# 	answer2 = input("What is the age and the name of the person (separated by space)? ")
# 	list_age.append(answer2.split())
# 	if int(list_age[0][0]) > 21:
# 		list_name.append(list_age[0][1])
# 	list_age.clear()

# print("The people allowed to see the movie are: ",*list_name)


#Ex13
# list_users = ["Mike", "David", "Dina"]
# list_allowed = []
# list_name = []
# list_age = []

# for x in list_users:
# 	answer2 = input("What is the age of " + x + "? ")
# 	if int(answer2) > 21:
# 		list_name.append(x)

# print("The people allowed to see the movie are: ",*list_name)


#Ex14
answer = ""
list_members = []

while answer != "quit":
	answer = input("You have 4 options: Add (to add a name) / Remove (to remove a name) / View (to see the family members) / Quit (to quit): ")
	if answer  == "Quit":
		print("Have a good day!")
		break
	elif answer == "Add":
		name = input("What is the name to add? ")
		list_members.append(name)
		continue
	elif answer == "Remove":
		remo =  input(" What is the name to remove? ")
		list_members.remove(remo)
		continue
	elif answer == "View":
		print("The family members are: ", *list_members)
		continue
	else:
		print("You entered a wrong option")

