import math
is_Prime = [True] * (2** 31)
is_Prime[0] = False
is_Prime[1] = False

tam= int(math.ceil(math.sqrt(len(a))))
for j in range(2,tam):
	if is_Prime[j]:
		for t in range(j+j, len(is_Prime), j):
			is_Prime[t] = False


n = int(raw_input())

for i in xrange(n):
	num = int(raw_input())
	if is_Prime[num]:
		print "Prime"
	else:
		print "Not Prime"



