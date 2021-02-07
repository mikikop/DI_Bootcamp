# #Ex1
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def find_oldest (cat1, cat2, cat3):
#     	if cat1.age >cat2.age and cat1.age > cat3.age:
#     		 return (cat1.name,cat1.age)
#     	elif cat2.age >cat1.age and cat2.age > cat3.age:
#     		return (cat2.name,cat2.age)
#     	elif cat3.age >cat1.age and cat3.age > cat2.age:
#     		return (cat3.name,cat3.age)



# cat1 = Cat("Kitty", 5)
# cat2 = Cat("Titty", 6)
# cat3 = Cat("Pitty", 10)


# (oldest_animal_name,oldest_animal_age) = find_oldest(cat1,cat2,cat3)

# print (f"The oldest cat is {oldest_animal_name}, and is {oldest_animal_age} years old")


#Ex2
# class Dog:
# 	"""docstring for Dog"""
# 	def __init__(self, name,height):
# 		super(Dog, self).__init__()
# 		self.name = name
# 		self.height = height

# 	def bark(self):
# 		print(f"{self.name} goes woof!")

# 	def jump(self):
# 		print(f"{self.name} jumps {self.height *2}cm high!")

# davids_dog = Dog("Rex",50)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)
# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
# 	print(f"The bigger dog is {davids_dog.name}")
# else:
# 	print(f"The bigger dog is {sarahs_dog.name}")

#Ex3
# class Song:
# 	"""docstring for Song"""
# 	def __init__(self, lyrics):
# 		super(Song, self).__init__()
# 		self.lyrics = lyrics

# 	def sing_me_a_song(self):
# 		for song in self.lyrics:
# 			print(f"{song}")

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()

#Ex4
class Zoo:
	"""docstring for Zoo"""
	def __init__(self, zoo_name):
		super(Zoo, self).__init__()
		self.name = zoo_name
		self.animals = []
		self.animals_sorted = {}

	def add_animal(self, new_animal):
		if new_animal in self.animals:
			print('The animal is already in the list')
		else:
			self.animals.append(new_animal)

	def get_animals(self):
		print(self.animals)

	def sell_animal(self,animal_sold):
		if animal_sold in self.animals:
			self.animals.remove(animal_sold)

	def sort_animals(self):
		self.animals.sort()
		master_list = []
		for animal in self.animals: #("cat", "dog")
			if not master_list:
				master_list.append([animal]) #[["cat","cougar"],["deer",""]]
			else:
				flag = False
				for sublist in master_list:
					if sublist[0][0]== animal[0]:
						sublist.append(animal) 
						flag = True
				if not flag:
					master_list.append([animal])
		for index,sublist in enumerate(master_list):
			self.animals_sorted.update({index+1:sublist})


zoo = Zoo("myzoo")
zoo.add_animal("cat")
zoo.add_animal("cougar")
zoo.add_animal("deer")
zoo.add_animal("dog")
zoo.add_animal("ape")


zoo.sort_animals()
print(zoo.animals_sorted)

