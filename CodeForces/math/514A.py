# coding: utf-8
#Author: Mariana Mendes.
#Problem 514A  Chewbaсca and Number*/

   
n = raw_input()
ans = ""

if(n[0] == '9'):
	ans+= '9'
elif(int(n[0]) <= 4):
	ans+= n[0]
else:
	ans+= str((9 - int(n[0])))

for i in xrange(1,len(n)):
	if(int(n[i]) <= 4):
		ans+= n[i]
	else:
		ans+= str((9 - int(n[i])))
	
	
print ans
