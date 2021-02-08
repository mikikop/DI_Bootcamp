class Family:
    """docstring for Family"""
    def __init__(self, members,last_name):
        super(Family, self).__init__()
        self.members = members
        self.last_name = last_name

    def born(self,**kwargs):
        #First way SO GOOD
        # born_dict = {**kwargs}
        # print(born_dict)

        #Second way Also Good
        # born_dict = {}
        # for key,arg in kwargs.items():
        #     born_dict.update({key:arg})

        self.members.append(kwargs)
        print("Congrats for the new baby!!")

    def is_18(self, name):
        for item in self.members:
            if item["name"]==name:
                if item["age"] >18:
                    print(f'{item["name"]} is more than 18')
                    return True
                    
                else:
                    print(f'{item["name"]} is younger than 18')
                    return False


    def info(self):
        string = [] 
        for item in self.members:
            print(item["name"],item["age"],item["gender"],item["is_child"])




if __name__ == "__main__":

    member = Family([{'name':'Michael','age':35,'gender':'Male','is_child':False},{'name':'Sarah','age':32,'gender':'Female','is_child':False}], "Cohen")


    member.born(name="Bob", age=1, gender="Male", is_child=True)

    member.info()

    member.is_18("Michael")
    member.is_18("Bob")









