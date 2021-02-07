class MenuManager:
	"""docstring for MenuManager"""
	def __init__(self, menu):
		super(MenuManager, self).__init__()
		self.menu = menu

	def add_item(self,name,price,spice,gluten):
		menu_dict = {}
		menu_dict["name"] = name
		menu_dict["price"] = price
		menu_dict["spice"] = spice
		menu_dict["gluten"] = gluten
		self.menu.append(menu_dict)
	
	def update_item(self,name,price,spice,gluten):
		for nameitem in self.menu:
			if nameitem["name"]==name:
				nameitem["price"] = price
				nameitem["spice"] = spice
				nameitem["gluten"] = gluten
		else:
			print("This dish is not in the menu")

	def remove_item(self,name):
		for nameitem in self.menu:
			if nameitem["name"]==name:
				self.menu.remove(nameitem)
				print(f'The menu is composed of {", ".join(self.menu)}')
			else:
				print("This dish is not in the menu")


menu = MenuManager([])

menu.add_item("Soup",10,"B",False)
menu.add_item("Hamburger",15,"A",True)
menu.add_item("Salad",18,"A",False)
menu.add_item("French Fries",5,"C",False)
menu.add_item("Beef bourguignon",25,"B",True)

menu.update_item("Soup",23,"A",True)

menu.remove_item("Salad")

print(menu.menu)