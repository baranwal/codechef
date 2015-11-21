t = int(raw_input())
a = []
for i in range(0,t):
	q,p = map(int,raw_input().split())
	if q <= 1000:
		tot_exp = float(q * p)
	else:
		tot_exp = float(q * p * 0.9)
	a.append(tot_exp)
for i in a:
	print format(i, '.6f') 
