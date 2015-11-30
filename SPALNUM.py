number = []
for i in range(int(raw_input())):
	a,b = map(int, raw_input().split())
	sum1 = 0
	for i in range(a,b+1):
		num = str(i)
		if num == num[::-1]:
			sum1 += int(num)
	print sum1		
