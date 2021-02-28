import sqlite3 as sl


class MenuItem:

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def run_query(self,query):
        connection = sl.connect('myrestaurant.db')
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def save(self):
        try:
            query = f"INSERT INTO mymenu (item,price) VALUES ('{self.name}','{self.price}')"
            self.run_query(query)
        except:
            return False

    def delete(self):
        query = f"DELETE FROM mymenu WHERE item = '{self.name}'"
        self.run_query(query)
    
    def update(self,new_name,new_price):
        query = f"UPDATE mymenu SET item = '{new_name}' WHERE item ='{self.name}'"
        self.run_query(query)
        query = f"UPDATE mymenu SET price = '{new_price}' WHERE item ='{new_name}'"
        self.run_query(query)

    @classmethod
    def all(cls):
        query = "SELECT item, price FROM mymenu"
        connection = sl.connect('myrestaurant.db')
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        if results:
            return results
        return "Database is empty"
    
    @classmethod
    def get_by_name(cls,item):
        query = f"SELECT * FROM mymenu WHERE item = '{item}'"
        connection = sl.connect('myrestaurant.db')
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        if results:
            return results
        return "Item is not in the DB"