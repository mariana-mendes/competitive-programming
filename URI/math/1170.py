while True:
	try:
		n = raw_input().split(" ")
		if int(n[1]) >= int(n[0]):
			print (int(n[1]) - int(n[0]))
		else:
			print (int(n[0]) - int(n[1]))
			
	except EOFError:
		break
