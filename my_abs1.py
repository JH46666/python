#!/usr/bin/env python
# -*- coding: utf-8 -*-
def my_abs(x):
    if x>=0:
	return x	
    else:
    	return -x


print u'请输入数字:'
x=raw_input();#x is str
d=int(x)
xx=my_abs(d)

print u'%s的绝对值是%d' %(x,xx)
