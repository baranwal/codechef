for i in range(int(raw_input())):
	n1 = int(raw_input())
	arr = map(int, raw_input().split())
	n2 = int(raw_input())
	arr1 = map(int, raw_input().split())
	try:
		n1 = arr.index(n1)
		n2 = arr1.index(n2)
	except ValueError:
		n1 = ''
		n2 = ''
	if n1 != '' and n2 != '':
		print 'Yes'
	else:
		print 'No'
