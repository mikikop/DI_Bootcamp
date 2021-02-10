#Ex1
# import random
# from cprint import cprint

# new_list = []

# def get_words_from_file():
# 	data = []
# 	new_data = []
# 	with open ("sowpods.txt", "r") as f:
# 		data = f.readlines()
# 	for word in data:
# 		word = word.strip('\n')
# 		new_data.append(word)
# 	return new_data

# def get_random_sentence(length):
# 	data = get_words_from_file()
# 	new_list = random.sample(data,length)
# 	my_string = (' '.join(new_list)).lower()
# 	return my_string


# def main():
# 	print ("We create a program that will generate a random sentence and display it to the you. We will allow you to choose how long the sentence will be.")
# 	answer = int(input("Please enter the number of words you want the sentence will be composed with (between 2 and 20): "))
# 	if answer not in range(2,21):
# 		cprint.err("You need to enter a number between 2 and 20")
# 		exit()
# 	else:
# 		sentence = get_random_sentence(answer)
# 		print('\033[1m'+ "Your sentence is: "+'\033[0m'+ '\033[94m' + sentence+'\033[0m')


#Ex2
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data = json.loads(sampleJson)
print(data["company"]["employee"]["payable"]["salary"])

data["company"]["employee"]["birth_date"] = '01/21/2021'

with open('jfile2.json','w') as f:
	json.dump(data,f)
