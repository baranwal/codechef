n1,n2 = map(float , raw_input().split())
if n1 > n2 or n1 == 0:
	print("%.2f" %n2)
else:
	if n1 % 5 != 0:
		print("%.2f" %n2)
	else:
		n1 = (n2 - n1) - 0.50
		if n1 < 0:
			print ("%.2f" %n2)
		else:
			print ("%.2f" %n1)

