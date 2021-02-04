# import random

# #Ex1
# def display_message():
# 	print("I'm studying python programming")

# display_message()


# #Ex2
# def favorite_book(title):
# 	print(f"One of my favorite books is {title}")

# favorite_book("Harry Potter")

# #Ex3
# def describe_city(city,country="France"):
# 	print(f"{city} is in {country}")

# describe_city("Reykjavik", "Iceland")
# describe_city("Jerusalem",'Israel')
# describe_city("Paris")

# #Ex4
# def compare_random(number):
# 	num_rand = random.randrange(1, 101)
# 	if number == num_rand:
# 		print("Great you guessed the right number")
# 	else:
# 		print(f"you failed! your number was {number} and the one to guess was {num_rand}")

# compare_random(55)

# #Ex5
# def make_shirt (size="L", message="I love Python"):
# 	print (f"The size you chose is {size} and the message you want to print on it is {message}")

# make_shirt("M","I'm a coder")
# make_shirt(message="I'm a coder", size="M")
# make_shirt()
# make_shirt("M")

# #Ex6
# magicians = ["Merlin", "Copperfield", "Hudini"]
# def show_magicians(my_list):
# 	print(f'The magicians that will make the show are {", ".join(my_list)}')

# show_magicians(magicians)

# def make_great(mag_list):
# 	for key in range(len(mag_list)):
# 		mag_list[key] = "the Great "+ mag_list[key]
# 	return mag_list

# magicians = make_great(magicians)

# show_magicians(magicians)


# #Ex7
# answer_gender = " "

# while answer_gender != "m" and answer_gender != "f":
# 	answer_gender = input("Please enter if you are a male(m) or a female(f): ")
# 	print(answer_gender)

# answer_birthdate  = input("Please enter your date of birth in that format (yyyy/mm/dd): ")


# def get_age(year,month,day):
# 	current_year = 2021
# 	current_month = 1
# 	if current_month < int(month):
# 		return (current_year - int(year) -1)
# 	else:
# 		return current_year - int(year)


# def can_retire(gender,date_of_birth):
# 	dateob = date_of_birth.split("/")
# 	person_age = get_age(dateob[0],dateob[1],dateob[2])
# 	if gender == "m":
# 		if person_age >=67:
# 			return True
# 		else:
# 			return False
# 	elif gender == "f":
# 		if person_age >=62:
# 			return True
# 		else:
# 			return False
# 	else:
# 		print("you enter a wrong information")


# retirement = can_retire(answer_gender,answer_birthdate)

# if retirement == True:
# 	print("You can retire")
# else:
# 	print("You can't right now retire")


#Ex8
def simple_cal(x):
	my_list = []
	my_sum = 0
	for i in range(1,5):
		my_list.append(x*i)
	for key in my_list:
		my_sum = my_sum + int(key)
	return my_sum

print(simple_cal("3"))



















