name = input('Enter a file name')
fhand = open(name)
d = {}
for line in fhand:
	if line.startswith('From'):
		words = line.split()
		if len(words)>1:
			word = words[1]
			if word not in d:
				d[word]=1
			else:
				d[word]+=1

print(d)
	