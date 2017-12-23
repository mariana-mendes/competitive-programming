# -*- coding: utf-8 -*-
# Mariana Mendes
# 1926 - Marianne and The Twin Cousins


import math

a = [True] * 10 ** 6
a[0] = False
a[1] = False

tam= int(math.ceil(math.sqrt(len(a))))
for j in range(2,tam):
	if a[j]:
		for t in range(j+j, len(a), j):
			a[t] = False




f = [0] * 10 ** 6

for i in range(2, len(a)-2): 
	if (a[i] and a[i-2]) or (a[i] and a[i+2]):
		f[i] = f[i-1] + 1
	else:
		f[i] = f[i-1]




n = int(raw_input())

for i in range(n):
	r = raw_input().split(" ")
	a = int(r[1])
	b = int(r[0])
	if a > b:
		print f[a] - f[b-1]
	else:
		print f[b] - f[a-1]
	
