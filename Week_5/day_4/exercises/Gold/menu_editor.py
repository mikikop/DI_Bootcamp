from menu_manager import Menu_Manager

    
def load_manager():
     return Menu_Manager()

def show_user_menu(new_menu):
    choice = ['a','d','v','x']
    answer = ''
    while answer not in choice:
        answer = input("Please enter an choice (a: add an item, d: delete an item, v: view the menu, x: exit): ")
        if answer == 'a':
            add_item_to_menu(new_menu)
        elif answer == 'd':
            remove_item_from_menu(new_menu)
        elif answer == 'v':
            show_restaurant_menu(new_menu)
        else:
            break

def add_item_to_menu(new_menu):
    name = input("give a name to your item: ")
    price = input("give a price to your item: ")
    if new_menu.add_item(name,price):
        print("Your item is saved!")
    else:
        print("There was an issue to save your item!")
    new_menu.save_to_file()

def remove_item_from_menu(new_menu):
    name = input("which item do you want to delete? ")
    if new_menu.remove_item(name):
        print("Your item is removed!")
    else:
        print("There was an issue to remove your item!")
    new_menu.save_to_file()

def show_restaurant_menu(new_menu):
    pass

new_menu = load_manager()