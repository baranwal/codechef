t = int(raw_input())
a = []
for i in range(0,t):
	n = int(raw_input())
	temp = n
	s = 0
	while temp:
		s *= 10
		s = s + temp % 10
		temp /= 10
	if n == s:
		a.append('wins')
	else:
		a.append('losses')
for i in a:
	print i
