#Exercises

#Ex1
print ("Hello world\n"*4)

#Ex2
print((99^3)*8)
print("\n")

#Ex3
#False
#True
#False
#error
#False

#Ex4
computer_brand = "apple"
print (f"I have an {computer_brand} computer")
print("\n")

#Ex5
name = "Michael"
age = 44
shoe_size = 42
info = print (f"I'm {name} and I'm {age} years old. My shoe_size is {shoe_size}")
print("\n")

#Ex6
a = 10
b = 5

if a > b:
	print("Hello World")
else:
	print("a is smaller than b")
print("\n")

#Ex7
num = int(input("Please enter a number: "))
if num % 2 == 0:
	print(f"The number {num} is even")
else:
	print(f"The number {num} is odd")
print("\n")

#Ex8
name = input("What is your name? ")
if name.capitalize() == "Mike":
	print("Hey such a beautiful name you have !")
else:
	print("your name is different than mine...Nobody is perfect !")
print("\n")


#Ex9
height = int(input("What is your height in inches? "))
cm_height = height * 2.54

if cm_height > 145:
	print("You're lucky ! you can ride this roller coaster...Enjoy!")
else:
	print("What can I say...maybe next year")