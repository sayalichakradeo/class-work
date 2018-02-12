fhand = open('mbox-short.txt')
fout = open('output.txt', 'w')
for line in fhand:
	fout.write(line)
print('copied successfully')