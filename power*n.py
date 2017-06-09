#!/user/bin/env python
# -*- coding:utf-8 -*-
def power(x,n):
	s=1
	while n > 0:
            n = n - 1
	    s = s * x
	return s

print u'请输入两个值'
x=raw_input();
n=raw_input();
c=int(x)
d=int(n)
xx=power(c,d)

print u'%s' %(xx)
