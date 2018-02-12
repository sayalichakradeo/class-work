fhand = open('words.txt')
d = {}
count = 0
for line in fhand:
	words = line.split()
	for word in words:
		d[word]=count
		count = count+1
print(d)