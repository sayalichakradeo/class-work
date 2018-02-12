fhand = open('mbox-short.txt')
count = 0
for line in fhand:
	if line.startswith('From'):
		words = line.split()
		if len(words)>2:
			count = count+1
			print(words[1])
			
		
	
print('there were ', count, ' no of lines starting with From')