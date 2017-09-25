while True:
	try:
		e = raw_input().split(" ")
		v = int(e[0])
		t = 2 *int(e[1])
		print v*t
	
	
	except EOFError:
		break
