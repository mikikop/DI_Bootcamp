import codexpEx1_2
from random import randint

class PetDog(codexp.Dog):
    """docstring for PetDog"""
    def __init__(self, name, age, weight):
        super().__init__(name,age,weight)
        self.trained = False

    def train(self):
        self.bark()
        self.trained = True

    # def play(self, *args):
    #         print('the dogs: ', *args, 'play together with ', self.name)
    #         #args.trained = False

    def play(self, *args):
            dogstr = ""
            for dog in args:
                dogstr += dog.name + " "
            print(f'the dogs: {dogstr} play together with ', self.name)
            #args.trained = False

    def do_a_trick(self):
        num = randint(1,4)
        if self.trained == True:
            if num == 1:
                print(f'{self.name} does a barrel roll')
            elif num == 2:
                print(f'{self.name} stands on their back legs')
            elif num == 3:
                print(f'{self.name} shakes your hand')
            elif num == 4:
                print(f'{self.name} plays dead')


petd1 = PetDog("dog1",5,6)
petd2 = PetDog("dog2",7,12)
petd3 = PetDog("dog3",1,1)

petd1.play(petd2,petd3)

petd1.train()
petd1.do_a_trick()

