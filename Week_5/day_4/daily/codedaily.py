from cprint import cprint
from time import process_time
import string

# with open ("the_stranger.txt", "r") as f:
# 	text = f.readlines()


class Text():

	def __init__(self, my_string, words = '',word_dict={}):
		self.my_string = my_string
		self.words = words
		self.words += ''.join(self.my_string)
		self.words = self.words.split()
		self.word_dict = word_dict

	def __repr__(self):
		print(self.words)
	
	def frequency(self,a_word):
		count = 0
		for word in self.words:
			if word == a_word:
				count += 1
		return count

	def string_dict(self):
		for word in self.words:
			if word not in self.word_dict.keys():
				self.word_dict[word] = 1
			else:
				self.word_dict[word] += 1
		return self.word_dict

	def most_frequent(self):
		max_list = []

		# for word in self.words:
		# 	if word not in self.word_dict.keys():
		# 		self.word_dict[word] = 1
		# 	else:
		# 		self.word_dict[word] += 1
		my_dict = self.string_dict()
		max_occ = max(my_dict.values())
		for key,value in my_dict.items():
			if value == max_occ:
				max_list.append((key,value))
		my_dict.clear()
		return max_list


	# def unique_words(self):
	# 	t1_start = process_time()
	# 	word_unique_list = []

	# 	# parsing all the text and for each word using the frequency() function
	# 	# and then parsing again the text to look for occurence == 1
	# 	# that means we could be not check all the words with more than
	# 	# 1 occurence. TAKES a REAL LONG TIME 
	# 	for word in self.words:
	# 		if self.frequency(word) == 1:
	# 			word_unique_list.append(word)

	# 	t1_stop = process_time()
	# 	t_final = t1_stop-t1_start
	# 	print("Elapsed time:", t1_stop, t1_start)  
	# 	print("Elapsed time: ",t_final)
	# 	return word_unique_list

	def unique_words(self):
		t1_start = process_time()
		word_unique_list = []

		# for each word in text, if the word is not in the dictionary put it
		# with occurence 1. If it is already in the list increment the value
		# Then, in the dictionary look for the values == 1 and put the key value in
		# a list. 40 times faster
		for word in self.words:
			if word not in self.word_dict.keys():
				self.word_dict[word] = 1
			else:
				self.word_dict[word] += 1

		for key,value in self.word_dict.items():
			if value == 1:
				word_unique_list.append((key,value))

		t1_stop = process_time()
		t_final = t1_stop-t1_start
		#print("Elapsed time:", t1_stop, t1_start)  
		print("Elapsed time: ",t_final)
		return word_unique_list


	@classmethod
	def from_file(self, my_file):
		with open (my_file, "r") as f:
			text = f.readlines()
		return Text(text)
	


class TextModification(Text):
	
	def __init__(self, my_string):
		super().__init__(my_string, words ='',word_dict={})
	
	def no_punct(self):
		new_list = []
		my_dict = self.string_dict()
		for word in my_dict.keys():
			new_list.append(word.translate(str.maketrans('','',string.punctuation)))
		return new_list












