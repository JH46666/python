def add_end(L=[ ]):
    if L is None:
        L = [ ]
	L.append('END')
	return L

L=raw_input();

gain=add_end(L)

print u'%s' %(gain)


