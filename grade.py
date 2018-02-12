def computegrade(score):
	if(score > 1.0 or score < 0):
		print('bad score')
	elif(score > 0.9):
		return 'A'
	elif(score > 0.8):
		return 'B'
	elif(score > 0.7):
		return 'C'
	elif(score > 0.6):
		return 'D'
	else:
		return 'F'

score = float(input('Enter the score\n'))
print('Your grade is: ',computegrade(score))