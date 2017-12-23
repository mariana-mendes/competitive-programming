# Mariana Mendes
# 588B - Duff in Love


import math

n = int(raw_input())
dv = []
raiz = int(math.floor(math.sqrt(n)))

for i in xrange(1,raiz+1):
	if(n%i == 0):
		dv.append(i)
		dv.append(n/i)

dv.sort(reverse=True)


ind = 0
ans = 1


while True:
	
	raiz = math.sqrt(dv[ind])
	
	if(raiz%1 == 0):
		ind+= 1
	
	resp = True
	atual = dv[ind]
	raiz = int(math.sqrt(atual))
		
	for t in xrange(2,raiz+1):
		if(atual%t == 0):			
			if(math.sqrt(t)%1 == 0 or math.sqrt(atual/t)%1 == 0):
				resp = False
				break
				
	if(resp):
		ans = atual
		break
	else:
		ind+=1	

print ans
