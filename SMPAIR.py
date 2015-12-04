for i in range(int(raw_input())):
	num = int(raw_input())
	arr = map(int, raw_input().split())
	arr.sort()
	print arr[0] + arr[1]
