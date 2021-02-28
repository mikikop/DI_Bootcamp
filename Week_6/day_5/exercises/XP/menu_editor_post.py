import psycopg2   # importing a module to connect to postgres
import psycopg2.extras

class MenuItem:

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def run_query(self,query):
        # defining our connection criteria
        HOSTNAME = 'localhost'
        USERNAME = 'postgres'
        PASSWORD = 'post'
        DATABASE = 'myrestaurant'
        # making the connection to the database
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def save(self):
        try:
            query = f"INSERT INTO menu (item,price) VALUES ('{self.name}','{self.price}')"
            self.run_query(query)
        except:
            return False

    def delete(self):
        query = f"DELETE FROM menu WHERE item = '{self.name}'"
        self.run_query(query)
    

    def update(self,new_price):
        # query = f"UPDATE menu SET item = '{new_name}' WHERE item ='{self.name}'"
        # self.run_query(query)
        query = f"UPDATE menu SET price = '{new_price}' WHERE item ='{self.name}'"
        self.run_query(query)

    @classmethod
    def all(cls):
        query = "SELECT item, price FROM menu"
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
        query = f"SELECT * FROM menu WHERE item = '{item}'"
        connection = sl.connect('myrestaurant.db')
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        if results:
            return results
        return "Item is not in the DB"