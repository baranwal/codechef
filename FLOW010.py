for i in range(int(raw_input())):
	char = raw_input()
	if char == 'B' or char =='b':
		print 'BattleShip'
	elif char == 'C' or char == 'c':
		print 'Cruiser'
	elif char == 'd' or char == 'D':
		print 'Destroyer'
	elif char == 'f' or char == 'F':
		print 'Frigate'
