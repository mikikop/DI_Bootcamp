#Ex1 Ex2 Ex3
# birthdays = {
# 	"Mike": "1977/03/21",
# 	"Noa": "2007/03/13",
# 	"Nathane": "2009/03/06",
# 	"Anael": "1983/02/16",
# 	"Tal": "2011/10/31"
# }


# answer_name = input("Give me please a person's name: ")
# answer_birthday = input("Give me please this person’s birthday (in the format “YYYY/MM/DD”): ")

# birthdays[answer_name] = answer_birthday

# list_keys = list(birthdays.keys())
# print('Hello! You can look up the birthday of the people in the list!')
# print(f'Here all the names I have in my memory {", ".join(list_keys)}')
# answer = input("Give me please a person's name: ")
# for name in birthdays:
# 	if answer == name:
# 		print(f"The {name}'s birthday is {birthdays[name]}")
# 		break
# else:
# 	print(f"Sorry, we don’t have birthday information for {answer}")


#Ex4
items = {}
item_list = ['banana','apple','orange','pear']
price_list = [4,2,1.5,3]

items = dict(zip(item_list,price_list))
print("Our list of fruits and prices is :")
for key in items:
	print(f"{key} : ${items[key]}")

items.update({'stock':{"banana":3,"apple":0,"orange":10,"pear":1}})
print(items)

total_cost = 0
item_price = 0

for item in items:
	# print("items: ",items[item])
	# print("stock: ",items['stock'][item])
	item_price = items[item]*items['stock'][item]
	total_cost = total_cost + item_price

print(f"The final cost for all the stock will be ${total_cost}")





