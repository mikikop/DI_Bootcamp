choice = input('Do you want to encrypt (e) or decrypt (d)? ')
cypher_text = ''
decypher_text = ''

if choice == 'e' or choice == 'E':
	e_message = input('Enter a message you want to encrypt: ')
	#encrypt with a shift right of 3
	for letter in e_message:
		if ord(letter) == 32:
			cypher_text += chr(ord(letter))
		else:
			cypher_text += chr(ord(letter)+3-26)
	print(cypher_text)
elif choice == 'd' or choice == 'D':
	d_message = input('Enter a message you want to decrypt: ')
	#decrypt
	for letter in d_message:
		if ord(letter) == 32:
			decypher_text += chr(ord(letter))
		else:
			decypher_text += chr(ord(letter)-3+26)
	print(decypher_text)
else:
	print("Sorry that's not an option. Retry!")


