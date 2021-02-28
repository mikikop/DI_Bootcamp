import sqlite3 as sl

con = sl.connect('test.db')

def get_details():
	name = input("What is your name? ")
	pin_number = input("What is your pin number? ")
	with con:
		query = f"SELECT * FROM employees WHERE first_name = '{name}' AND pin_number = '{pin_number}';"
		print(query)
		data = con.execute(query)
		for row in data:
			print(row)


# CREATE TABLE employees
# (
# 	id INTEGER PRIMARY KEY AUTOINCREMENT,
#   first_name TEXT,
#   last_name TEXT,
#   pin_number TEXT,
#   salary NUMERIC
# );
# INSERT INTO employees 
# (first_name, last_name, pin_number, salary)
# VALUES 
# ('Adam', 		'Adamson',	'aaa', 20000),
# ('Bobby', 	'Brown', 	'bbb', 25000),
# ('Charlie', 	'Chaplain', 'ccc', 33000),
# ('Davey', 	'Dobson', 	'ddd', 17000),
# ('Eli', 		'Emmerson', 'eee', 12000),
# ('Freddie', 	'Farrah', 	'fff', 22000)


# USE THIS AS PIN: ' or ''='
