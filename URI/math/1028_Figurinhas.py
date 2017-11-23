
def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)


n = int(raw_input())

for i in xrange(n):
	j = raw_input().split(" ")
	print gcd(int(j[0]), int(j[1]))





