# Author: Mariana Mendes.
# Problem 584A  The number of positions*/
   
   
n = map(long,raw_input().split(" "))
fim = long('9' * n[0])
ans = -1


while len(str(fim)) >= n[0] and fim != 0:
	if(fim%n[1] == 0):
		
			ans = fim
			break
	else:
		fim-=1
		
print ans
