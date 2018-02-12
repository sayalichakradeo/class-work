sum = 0
avg = 0
count = 0
while True:
	num = input('Enter a number: ')
	if num == 'done':
		break
	try:
		n1 = float(num)
		sum = sum + n1
		count = count + 1
	except:
		print('Please enter a valid number')
if count == 0:
	print(sum, ' ', count,' ',0)
else:
	print(sum, ' ', count,' ',sum/count)