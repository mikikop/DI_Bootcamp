#Ex1
# list1 = ["1","2","3"]
# list2 = ["a","b", 4]
# list1.extend(list2)
# print(list1)

#Ex2
# answer1 = input("Input the 1st number? ")
# answer2 = input("Input the 2nd number? ")
# answer3 = input("Input the 3rd number? ")

# list_num = []
# list_num.append(int(answer1))
# list_num.append(int(answer2))
# list_num.append(int(answer3))
# list_num.sort()
# print("The greatest number is: ",list_num[-1])

#Ex3
# alphabet = "abcdefghijklmnopqrstuvwxyz"


# for i in range(0,26):
# 	if alphabet[i] == "a" or alphabet[i] == "e" or alphabet[i] == "i" or alphabet[i] == "o" or alphabet[i] == "u":
# 		print(alphabet[i]," is a vowel")
# 	else:
# 		print(alphabet[i],' is a consonant')

#Ex4
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# answer = input("Input a name ")
# if answer in names:
# 	print("the index of ",answer, " is ",names.index(answer))

#Ex5
#in 1 line
#words = input("Input 7 words (separated by a space): ").split()

# answer = ""
# while len(answer.split()) != 7 :
# 	answer = input("Input 7 words (separated by a space): ")
# words = answer.split()	

# letter = input("Input a single char: ")

# for x in words:
# 	if letter in x:
# 		print("la lettre ",letter, " is at the index ",x.index(letter), " in the word ",x)
# 	else:
# 		print("the letter ", letter, " is not in those words")

#Ex6
# list_million = []
# for x in range(1,1000001):
# 	list_million.append(x)
# print(min(list_million))
# print(max(list_million))
# print(sum(list_million))

#Ex7
# list_seq = []
# tuple_seq = ()

# answer = input("Input a sequence of comma-separated numbers: ")

# list_seq = answer.split(",")
# print(list_seq)

# for x in list_seq:
# 	tuple_seq = tuple_seq + (x,)

# print(tuple_seq)


#Ex8
import random
answer = ""

while int(answer) not in xrange(1,10):
	answer = input("Input a number between 1 and 9: ")

random_num = random.randint(3,9)
print(random_num)



