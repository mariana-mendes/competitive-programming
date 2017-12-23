import math

# Mariana Mendes
# Pentagon - 2584


n  = int(raw_input())

for i in xrange(n):
	l = int(raw_input())
	angulo = math.tan((36*2*math.pi)/360.0)
	a = (l/2.0)/angulo
	total = (l * a)/2.0
	print "%.3f"%(total*5)
