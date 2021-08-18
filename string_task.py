def stringTask(string):
	string2=''
	for i in string:
		if i in 'aeiouy':
			string.replace(i, '')
			continue
		string2 += '.' + i

	print(string2)

string = input()
stringTask(string.lower())