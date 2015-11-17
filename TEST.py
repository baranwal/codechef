a = []
def code():
	no = input()
	if no != 42:
		if no/100 <=0: 
			a.append(no)
		code()
	else:
		for row in a:
			print row
		pass	
		return



code()
