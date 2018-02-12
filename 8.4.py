fhand = open("romeo.txt")
my_list=list()
for line in fhand:
	line = line.lower()
	words = line.split()
	for word in words:
		if word not in my_list:
			my_list.append(word)
my_list.sort()
print(my_list)