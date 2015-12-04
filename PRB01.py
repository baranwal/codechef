for i in range(int(raw_input())):
	num = int(raw_input())
	x = True
	for j in range(2,num):
		if num % j == 0:
			x = False
			break
	if x:
		print 'yes'
	else:
		print 'no'
