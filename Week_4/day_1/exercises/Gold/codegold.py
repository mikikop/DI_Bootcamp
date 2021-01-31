#Ex1
print ("Hello world\n"*4 + "I love python\n"*4)

#Ex2
month = int(input("please enter a month from 1 to 12: "))
if month >= 3 and month <=5:
	print(f"The season in month {month} is spring")
elif month >=6 and month <=8:
	print(f"The season in month {month} is summer")
elif month >=9 and month <=11:
	print(f"The season in month {month} is autumn")
else:
	print(f"The season in month {month} is winter")