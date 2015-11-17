n,k = raw_input().split(' ')
n = int(n)
k = int(k)
count = 0
a = []
for index in range(0,n):
	t = int(raw_input())
	a.append(t)
for row in a:
	if row % k == 0 and row != 0:
		count = count + 1
print count
