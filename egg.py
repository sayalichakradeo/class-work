inp = input('Enter the file name\n')
try:
	fhand = open(inp)
	count = 0
	for line in fhand:
		if line.startswith('Subject'):
			count = count+1
	print('the file has ',count, ' subjects')
except:
	if inp.startswith('nana'):
		print('oopsss!!!! no no!')
		exit()
	else:
		print('file cannot be opened: ',inp)
		exit()