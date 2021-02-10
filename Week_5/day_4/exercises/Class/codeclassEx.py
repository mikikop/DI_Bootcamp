with open ("emails.txt", "w") as f:
	#f.write("Here the list of the emails to send a note:\n")
	f.write("jon@gmail.com\nmike@gmail.com\ntom@yahoo.com")



with open ("emails.txt", "r") as f:
	#print(f.seek(5))
	data = f.readlines()
	#print(f.tell())

for person in data:
	person = person.strip('\n')
	print(f"Sending email to {person}")