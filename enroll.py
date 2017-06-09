#!/usr/bin/env python
# -*- coding: utf-8 -*-
def enroll(name,gender,age=6,city='beijing'):
	print 'name:',name
	print 'gender:',gender
        print 'age:',age
        print 'city:',city


print u'请输入你的值'
print 'student:'
name=raw_input();
gender=raw_input();


gain=enroll(name,gender)

