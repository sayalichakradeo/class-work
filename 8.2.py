fhand = open('mbox-short-modified.txt')
for line in fhand:
	words = line.split()
	if len(words) == 0 : continue
	if words[0] != 'From' : continue
	#for a file that might not have anything stored at words[2]
	if len(words)>2:
		print(words[2])