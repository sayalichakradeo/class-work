def count(word, letter):
	count = 0
	for l in word:
		if l == letter:
			count = count + 1
	return count
	
word = input('Enter the word\n')
letter = input('Enter the letter\n')		
print(count(word, letter))