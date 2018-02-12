name = input('Enter a file name')
fhand = open(name)
d = {}
for line in fhand:
	if line.startswith('From'):
		words = line.split()
		if len(words)>2:
			word = words[2]
			if word not in d:
				d[word]=1
			else:
				d[word]+=1

print(d)
	