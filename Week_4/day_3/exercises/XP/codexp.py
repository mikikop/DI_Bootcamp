#Ex1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# my_dict = dict(zip(keys,values))
# print(my_dict)

#Ex2
# family = {
# 	"rick": 43, 
# 	'beth': 13, 
# 	'morty': 5, 
# 	'summer': 8
# 	}
# cost_pers = 0
# total_cost = 0


# for name,age in family.items():
# 	if age>=12:
# 		cost_pers = 15
# 		total_cost = total_cost + 15
# 	elif age>3 and age<12:
# 		cost_pers = 10
# 		total_cost = total_cost + 10
# 	else:
# 		cost_pers = 0
# 		total_cost = total_cost + 0
# 	print(f"{name} will pay ${cost_pers}")

# print(f"The total cost for all the family will be {total_cost}")

#Bonus
# family2 = {}
# fam =[]
# answer = ''
# while answer != 'quit':
# 	answer = input('Please enter your name and your age (separated by a space) and quit to exit: ')
# 	if answer == 'quit':
# 		break
# 	myfam = answer.split()
# 	fam.append(myfam)

# family2 = dict(fam)	
# print(family2)
# cost_pers = 0
# total_cost = 0


# for name,age in family2.items():
# 	if int(age)>=12:
# 		cost_pers = 15
# 		total_cost = total_cost + 15
# 	elif int(age)>3 and int(age)<12:
# 		cost_pers = 10
# 		total_cost = total_cost + 10
# 	else:
# 		cost_pers = 0
# 		total_cost = total_cost + 0
# 	print(f"{name} will pay ${cost_pers}")

# print(f"The total cost for all the family will be ${total_cost}")

#Ex3
# brand = {
# 	'name': 'Zara',
# 	'creation_date': '1975',
# 	'creator_name': 'Amancio Ortega Gaona',
# 	'type_of_clothes': 
# 		(
# 			'men',
# 			'women',
# 			'children',
# 			'home'
# 		),
# 	'international_competitors': 
# 		[
# 			'Gap',
# 			'H&M',
# 			'Benetton'
# 		],
# 	'number_stores': 700,
# 	'major_color': 
# 		{
# 			'France': 'blue',
# 			'Spain': 'red',
# 			'US': 
# 				(
# 					'pink',
# 					'green'
# 				)
# 		}

# }

# #change the number of stores to 2
# brand['number_stores'] = 2
# #print(brand)

# #who are the Zara clothes. the join() method can be used on tuple
# clothes = brand['type_of_clothes']
# print(f'The clothes of Zara are for {" and for ".join(clothes)}')

# #add the key country_creation with value Spain
# brand.update({'country_creation':'Spain'})

# #add a value to an existing key without to overwrite the other values
# brand.setdefault('international_competitors',[]).append('Desigual')

# #delete a key:value
# del brand["creation_date"]

# #print the last international competitor
# print(brand['international_competitors'][-1])

# #print the major color clothes in the us
# color1 = brand['major_color']['US'][0]
# color2 = brand['major_color']['US'][1]
# print(f'The major clothes’ colors in the US are {color1} and {color2}')

# #amount of key:values
# print(len(brand))

# #print the key of the dict
# print(brand.keys())

# #second dict
# more_on_zara = {
# 	'creation_date': '1975',
# 	'number_stores': 10000
# 	}

# #add the info of the second dict to the first one
# brand.update(more_on_zara)

# #print number stores -- the previous number was overwritten
# print(brand['number_stores'])


#Ex4
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 
disney_users_A = {}
disney_users_B = {}
disney_users_C = {}
disney_users_D = {}
i = 0
j = 0
k = 0

#1 output
for key in users:
	disney_users_A[key]= i
	i +=1
print(disney_users_A)


#2 output
for i in range(len(users)):
	disney_users_B[i]=users[i]
print(disney_users_B)

#3
users.sort()
for key in users:
	disney_users_C[key]= j
	j +=1
print(disney_users_C)

#4 NOT FOUND HOW TO GET A CHAR FROM A STRING IF IT EXISTS
for key in users:
	if key[0] == "M" or key[0] == "P":
		disney_users_D[key]= k
		k +=1
print(disney_users_D)



