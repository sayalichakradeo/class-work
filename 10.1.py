name = input('Enter a file name')
fhand = open(name)
d = {}
for line in fhand:
	if line.startswith('From'):
		words = line.split()
		if len(words)>0:
			word = words[1].split('@')
			if word[1] not in d:
				d[word[1]]=1
			else:
				d[word[1]]+=1
mylist = list()
for k,v in d.items():
	mylist.append((v,k))

mylist.sort(reverse=True)
print(mylist[:1])

	