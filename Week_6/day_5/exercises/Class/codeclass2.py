import sqlite3 as sl

def update(data):
	cursor = connection.cursor()
	query = f"SELECT quantity FROM fruits WHERE fruit = '{data}'"
	cursor.execute(query)
	# fetching the results
	results = cursor.fetchall()
	quantity = results[0][0] + 1
	query = f"UPDATE fruits SET quantity = {quantity} WHERE fruit = '{data}'"
	cursor.execute(query)
	connection.commit()

def add(data):
	try:
		cursor = connection.cursor()
		query = f"INSERT INTO fruits (fruit, quantity) VALUES ('{data}', 1)"
		cursor.execute(query)
		connection.commit()
	except:
		update(data)
	print("Saved!")

def connect():
	return sl.connect('database.db')

def disconnect():
	connection.close()



connection = connect()

while True:
	fruit = input("Enter a fruit: ")
	if fruit == 'quit':
		break	
	add(fruit)
	
print('bye')
disconnect()