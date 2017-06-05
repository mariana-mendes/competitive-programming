import math

h = float(raw_input())
dist = raw_input()
p1 = int(dist[0])
p2 = int(dist[1])
n = int(raw_input())

for i in xrange(n):
	a = raw_input().split(" ")
	alphaRad = (float(a[0]) * 3.14159)/180
	v = float(a[1])
	d = ((v*v) * math.sin(2*alphaRad))/(2*9.80665)
	e = 1 + math.sqrt( 1+  ((2*9.80665*h) / (v*v) * math.sin(alphaRad)**2))
	print "%0.5f"%(e*d)
	
