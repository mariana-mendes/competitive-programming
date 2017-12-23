# Mariana Mendes
# 230B - T-primes


import math


f = [True] * ((10**6)+1)
f[0] = False
f[1] = False


tam= int(math.ceil(math.sqrt(len(f))))
for i in range(2,tam):
	if(f[i]):
		for j in range(i+i, len(f), i):
			f[j] = False
			
				


n = int(raw_input())
a = map(int, raw_input().split(" "))


for l in a:
	raiz = math.sqrt(l)
	if(raiz%1 == 0):
		ans = (f[int(raiz)])
	else:
		ans = False
		
	if(ans):
		print "YES"
	else:
		print "NO"
