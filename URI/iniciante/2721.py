# Mariana Mendes
# Indecisao das Renas | 2721


renas = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]
num = map(int, raw_input().split())
total = sum(num)

if(total%9 == 0):
	print "Rudolph"
else:
	print renas[(total%9)-1]
