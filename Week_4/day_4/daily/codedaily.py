sentence = '7i3Tsih%xi #sM $a #t%^r!'

string_result = ""
string1 = ""
string2 = ""
string3 = ""

for i in sentence[0:22:3]:
	string1 = string1 + i
print("string1: ",string1)
for i in sentence[1:23:3]:
	string2 = string2 + i
print("string2: ",string2)
for i in sentence[2:24:3]:
	string3 = string3 + i
print("string3: ",string3)
	
for i in string1:
	if i.isalpha():
		string_result += i

for i in string2:
	if i.isalpha():
		string_result += i

for i in string3:
	if i.isalpha():
		string_result += i

print(string_result)