max = None
min = None
while True:
	num = input('Enter a number: ')
	if num == 'done':
		break
	try:
		n1 = float(num)
		if max is None or n1 > max:
			max = n1
		if min is None or n1 < min:
			min = n1
	except:
		print('Please enter a valid number')

print(max, ' ', min,' ')