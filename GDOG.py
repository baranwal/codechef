for i in range(int(raw_input())):
	a,b = map(int, raw_input().split())
	max1 = 0 
	for j in range(1,b+1):
		if a % j > max1:
			max1 = a % j
	print max1
