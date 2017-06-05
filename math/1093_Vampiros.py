import math

def prob(ev1,ev2, at, d):
	p = at/6
	q = 1 - p
	if at == 3:
		p2 = ev1/(ev1+ev2)
	else:
		p2 = (1 - (q/p)**ev1) / (1 - (q/p)**(ev1+ev2))

	return "%0.1f"% (p2*100)



	
while(True):
	s = raw_input().split(" ")
	
	ev1 = float(s[0])
	ev2 = float(s[1])
	at = float(s[2])
	d = float(s[3])

	if ev1 == 0 and ev2 == 0 and at == 0 and d ==0:
		break

	if d == 1:
		print prob(ev1, ev2, at, d)
	
	else:
		ev1 = math.ceil(ev1/d)
		ev2 = math.ceil(ev2/d)
		print prob(ev1, ev2, at, d)

	

	
