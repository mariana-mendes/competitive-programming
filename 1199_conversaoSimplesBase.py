while True:
	e = raw_input()
	if 'x' not in e and int(e) < 0:
		break		
	if len(e) > 2 and e[1] == "x":
		print int(e[2:len(e)], 16)
	else:
		resp = hex(int(e))
		ans = resp[0:2]		
		for i in xrange(2, len(resp)):
			ans += resp[i].upper()

		print ans 


