def fatorial(a):
	if a == 0:
		return 1
	else:
		return fatorial(a-1)*a


while True:
    try:
        i = raw_input().split(" ")
	print fatorial(int(i[0])) + fatorial(int(i[1]))
    except EOFError:
        break
