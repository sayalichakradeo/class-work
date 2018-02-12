file = input('Please enter valid file: ')
fhand = open(file)
print('File does not exist')

d = {}
for line in fhand:
	line=line.lower()
	for letter in line:
		if letter not in 'abcdefghijklmnopqrstuvwxyz':
			continue
		if letter not in d:
			d[letter]=1
		else:
			d[letter]=d[letter]+1
		
mylist=list()
for k,v in d.items():
	mylist.append((k,v))
mylist.sort(reverse = True)

for k,v in mylist:
	print(k,v)