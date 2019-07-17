# make a dictinoary from a string

def makeAdict(myString):
	new_dict = {}
	for i,word in enumerate(myString):
		new_dict[word] = [1,i]
	return new_dict
# make a string from a dictionary

def makeStringFromDictionary(myDict):
	tempStr =""

	for i in sorted(myDict.items(), key = lambda i : i[1][1]):
		tempStr+=i[0]
	return tempStr

myDict ={'r' :[1,4], 'o':[1,3], 'w': [1,0], 'd': [1,5]}

#word_dict =makeAdict("word")
#print(word_dict)
print(makeStringFromDictionary(myDict))
