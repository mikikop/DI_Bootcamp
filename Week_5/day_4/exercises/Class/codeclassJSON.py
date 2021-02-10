import json

# load       read json from a file and convert to pyhton
# loads s is for string....convert a json string to python

# dump convert from python to json and write to file
# dumps convert from python to a json string


thing = [
	{
		'name': 'bob',
		'age': 55,
		'stuff': True
	},
	{
		'nums': [1,2,3],
		'letter': ['a','b','c']
	},
]


with open('jfile.txt','w') as f:
	json.dump(thing,f)

with open('jfile.txt','r') as f:
	thing2 = json.load(f)