t = int(raw_input())
a = []
for index in range(0,t):
	b = 1
	n = int(raw_input())
	if n == 1:
		a.append(n)
	else:
		for i in range(1,n+1):
			b = b*i
		a.append(b)
for row in a:
	print row
