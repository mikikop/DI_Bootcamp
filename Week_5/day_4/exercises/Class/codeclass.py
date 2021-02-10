with open ("blah.txt", "w") as f:
	f.write("Hello\n")

with open ("blah.txt", "w") as f:
	f.write("Goodbye\n")

with open ("blah.txt", "a") as f:
	f.write("great")

with open ("blah.txt", "r") as f:
	data = f.read()


with open ("blah.txt", "r") as f:
	data = f.readlines()

# w write
# r read
# a append
# w+ write + read
# a+ append +read

# Writing....
# f.write() Writes a string to the file
# f.writelines() Writes a list to the file, line by line


# Reading..
# f.read()		Reads the entire file into a single string
# f.readline()	Reads a single line
# f.readlines() Reads the entire file into a list of strings

