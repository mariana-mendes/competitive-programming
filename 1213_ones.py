while True:
	try:
		num = int(raw_input())
		comp = "1"
		while True:
			if int(comp) > num and int(comp)%num == 0:
				print len(comp)
				break
			else:
				 comp += "1"
	

	except EOFError:
		break
