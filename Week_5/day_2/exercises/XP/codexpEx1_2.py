#Ex1
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Persian(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# my_cats = [Bengal("titi",3), Chartreux("polo",5), Persian("chang",8)]

# my_pets = Pets(my_cats)

# my_pets.walk()


#Ex2
class Dog():
    """docstring for Dog"""
    def __init__(self, name, age, weight):
        super(Dog, self).__init__()
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return "woof, woof,woof"

    def run_speed(self):
        return (self.weight/self.age)*10

    def fight(self, other_dog):
        if other_dog.run_speed() > self.run_speed():
            return (f'{other_dog.name} is the winner')
        else:
            return (f'{self.name} is the winner')

# dog1 = Dog("bob",3,5)
# dog2 = Dog("dolly",6,7)
# dog3 = Dog("neil",12,8)

# print(dog1.bark())
# print(dog1.name,dog1.run_speed())
# print(dog2.name,dog2.run_speed())
# print(dog3.name,dog3.run_speed())

# print(dog1.fight(dog2))
# print(dog1.fight(dog3))
# print(dog3.fight(dog2))


        