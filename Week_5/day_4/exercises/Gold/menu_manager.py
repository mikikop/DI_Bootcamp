import json

class Menu_Manager:

    def __init__(self):
        with open('menu.json') as f:
	        self.menu = json.load(f)
    
    def add_item(self,name, price):
        try:
            new_item = {'name':name, 'price':price}
            self.menu['items'].append(new_item)
            return True
        except:
            return False

    def remove_item(self,name):
        for item in self.menu['items']:
            if item['name'] == name:
                self.menu['items'].remove(item)
                return True
        return False
    
    def save_to_file(self):
        with open('menu.json', 'w') as json_file:
            json.dump(self.menu, json_file)