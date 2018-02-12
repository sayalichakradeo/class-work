
mylist = list()
while True:
	num = input('Enter a number: ')
	if num == 'done':
		break
	try:
		n1 = float(num)
	except:
		print('Enter a valid number\n')
		continue
	mylist.append(n1)
	
print(mylist)
print('Maximum: ',max(mylist))
print('Minimum: ',min(mylist))