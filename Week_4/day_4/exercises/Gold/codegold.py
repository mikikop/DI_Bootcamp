import random

# my_season = {
# 	'winter': [1,2,3],
# 	'spring': [4,5,6],
# 	'summer': [7,8,9],
# 	'autumn': [10,11,12]
# }

# def get_random_temp(season):
# 	if season.lower() == 'winter' or int(season) in my_season['winter']:
# 		return random.randrange(-10, 17)
# 	elif season.lower() == 'spring' or int(season) in my_season['spring']::
# 		return random.randrange(10, 21)
# 	elif season.lower() == 'summer' or int(season) in my_season['summer']::
# 		return random.randrange(15, 40)
# 	elif season.lower() == 'autumn' or int(season) in my_season['autumn']::
# 		return random.randrange(5, 25)
# 	else:
# 		print(f"Which {season} is it??")

# def main():
# 	season = input('Please choose a season to get advices (winter/spring/summer/autumn) or you can also choose a month (from 1 to 12): ')
# 	temp = float(get_random_temp(season))
# 	print(f"The temperature right now is {temp} degrees Celsius")
# 	if temp < 0:
# 		print("Brrr, that’s freezing! Wear some extra layers today”")
# 	elif temp >=0 and temp < 16:
# 		print("Quite chilly! Don’t forget your coat")
# 	elif temp >=16 and temp <23:
# 		print("Spring is here!")
# 	elif temp >=23 and temp < 32:
# 		print("Summer is coming")
# 	else:
# 		print("You can't breath!")

# main()


#Ex2
def throw_dice():
	return random.randrange(1, 6)

def throw_until_doubles():
	counter = 1
	throw1 = throw_dice()
	throw2 = throw_dice()
	throw_list = [(throw1,throw2)]
	while throw1 != throw2:
		throw1 = throw_dice()
		throw2 = throw_dice()
		throw_list.append((throw1,throw2))
		counter += 1
	return counter, throw_list

def main():
	main_list = []
	for i in range(0,100):
		main_list.append(throw_until_doubles())
		print(f'{i+1}. {" ".join(str(main_list[i][1]))}')
	count_throws = 0
	for i in range(0,100):
		count_throws += main_list[i][0]
	avg = round(count_throws/100,2)
	print(count_throws)
	print(avg)

main()




