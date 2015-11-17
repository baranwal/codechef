t = int(raw_input())
for i in range(0,t):
	A,B = map(int,raw_input().split())
	d = abs(A-B)
	max1 = A if A > B else B
	d = 2 * max1 - d
	print max1,d

