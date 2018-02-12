def computepay( h,  r):
	if (h > 40):
		extra = h-40
		result = 40*r + extra*(r/2)
	else:
		result = h*r
	return result;
	

try:
	h = float(input('Enter hours\n'))
	r = float(input('Enter rate\n'))
	print('Pay: ', computepay(h,r))

except:
	print('Please enter a number')

