file = input('Please enter valid file: ')
fhand = open(file)
print('File does not exist')

d = {}
for line in fhand:
	words = line.split()
	if len(words) > 0 and words[0] == 'From':
		d1,d2,d3 = words[5].split(':')
		if d1 not in d:
			d[d1] = 1 
		else:
			d[d1] += 1

mylist = list()
for k, v in d.items():
	mylist.append((k, v))

mylist.sort()
for k, v in mylist :
	print(k, v)
		