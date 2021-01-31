import random

new_str = input("please enter a string: ")
len_str = len(new_str)
first_char = new_str[0]
last_char = new_str[9]


if len_str < 10:
	print("Sorry string not long enough")
elif len_str > 10:
	print("Sorry string too long")
else:
	print(f"perfect string\n. Your first characters is {first_char} and your last char is {last_char} ")

i=0
while i < len_str:
    print(new_str[0:i+1])
    i+=1

str_list = list(new_str)
random.shuffle(str_list)
#print(str_list)
print(''.join(str_list))

#random.shuffle(list(new_str))
#print(list(new_str))






