def chop(mylist):
	mylen = len(mylist)
	print(mylist[1:mylen-1])
	return None
	
def middle(mylist):
	mylen = len(mylist)
	return mylist[1:mylen-1]
	
	
	
mylist = ['a', 'b', 'c','d']
print('Executing chop function:\n')
chop(mylist)
print('Executing middle function:\n')
middlelist = middle(mylist)
print(middlelist)