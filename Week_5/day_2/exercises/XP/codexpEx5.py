import codexpEx4




class TheIncredibles(Family):
    """docstring for TheIncredibles"""
    def __init__(self, members,last_name,power,incredible_name):
        super().__init__(members,last_name)
        self.members["power"] = power
        self.members["incredible_name"] = incredible_name

    def use_power(self,member):
        try:
            if member.is_18():
                print(member.power)
        except:
            print("You have no power here !!")

    def incredible_presentation(self):
        for item in self.members:
            print("member: ", item["name"], " and powers: ",item["power"])
    


    Family = TheIncredibles([{'name':'Mr. Incredible','age':35,'gender':'Male','is_child':False},{'name':'Sarah','age':32,'gender':'Female','is_child':False}], "Cohen")