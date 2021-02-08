import codexpEx4




class TheIncredibles(Family):
    """docstring for TheIncredibles"""
    def __init__(self, members,last_name,power,incredible_name):
        super().__init__(members,last_name)
        self.power = power
        self.incredible_name = incredible_name

    def use_power(self,member):
        try:
            if member.is_18():
                print(member.power)
        except:
            print("You have no power here !!")

    def incredible_presentation(self):
        for item in self.members:
            for key,value in item.items():
            print("members: ", member, " and powers: ",)
        