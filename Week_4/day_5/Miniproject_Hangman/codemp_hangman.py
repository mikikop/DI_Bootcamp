import getpass
word_hidden = []
word_to_find = []
guesses = 10
isWinner = False


print("The goal of the game is simple. \nThe first player enter a word to discover. \nThe second one has 10 guesses to find out it. Good luck! \n")

#Ask a player to enter a word to discover
def ask_for_a_word():
	answer=""
	while answer.isalpha() == False :
		print ("Please enter a word to find out: ")
		answer = getpass.getpass(prompt="Your word?",stream=None) #input('Please enter a word to find out: ')
	word_to_find = list(answer)
	return word_to_find


#Ask a letter to the player and check if it's a legal char 
def ask_for_a_letter():
	answer=""
	while answer.isalpha() == False or len(answer) !=1 :
		answer = input('\n Please enter only one letter: ')
	return answer

#Check if the letter is in the word and at which position(s). return a list with positions or an empty one
def check_position(letter, word):
	pos_list = []
	for i in range(len(word)):
		if word[i] == letter:
			pos_list.append(i)
	return pos_list

#display the board
def display_board(word_to_find,word_hidden,original_guesses):
	letter = ask_for_a_letter()
	pos = check_position(letter,word_to_find)
	if len(pos) == 0:
		if original_guesses > 0:
			original_guesses -= 1
			print("\n" + '\033[91m' + "Wrong choice!" +'\033[1m'+ f"{original_guesses} more guesses" + '\033[0m')
			return original_guesses, False
		else:
			return original_guesses, False
	else:
		if original_guesses > 0:
			if "*" not in word_hidden:
				return original_guesses, True
			else:
				for i in pos:
					word_hidden[i]=word_to_find[i]
				print('\n' +'\033[36m'+ 'Good choice! => '+'\033[0m' + '\033[1m' +'\033[94m' +f'{"".join(word_hidden)}' + '\033[0m')
				if "*" not in word_hidden:
					return original_guesses, True
				else:
					return original_guesses, False


#MRun the program
word_to_find = ask_for_a_word()
for i in range(0,len(word_to_find)):
	word_hidden.append("*")
print("".join(word_hidden))


while guesses > 0 and isWinner == False:
	guesses, isWinner  = display_board(word_to_find,word_hidden,guesses)

if guesses == 0:
	print('\033[36m' + "You loose man! Maybe next time" + '\033[0m')

if isWinner == True:
	print('\033[95m' + "You win, champ!" + '\033[0m')



