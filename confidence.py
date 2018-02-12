inp = input('Enter the file name')
fhand = open(inp)
total = 0
count = 0
for line in fhand:
	if line.startswith('X-DSPAM-Confidence'):
		pos = line.find(':')
		conf = float(line[pos+1:])
		total = total + conf
		count = count+1
print('Average spam confidence: ',total/count)