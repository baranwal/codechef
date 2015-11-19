t = int(raw_input())
a = []
for i in range(0,t):
	n = int(raw_input())
	s = 0
	while n:
		s += n % 10
		n /= 10
	a.append(s)
for i in a:
	print i
