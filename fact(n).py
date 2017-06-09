def fact(n):
	if n==1:
	    return 1
	return n * fact(n-1)

n=raw_input();
gain=fact(int(n))

print u'%d' %(gain)
