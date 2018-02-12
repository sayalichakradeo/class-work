fhand = open("romeo.txt")
mylist = []
for line in fhand:
	word = line.split()
	for w in word:
		if w not in mylist:
			mylist.append(w)

mylist.sort()
print (mylist)
