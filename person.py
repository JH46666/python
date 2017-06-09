def person(name,age,**kw):
	print 'name:',name, 'age:',age, 'other:',kw


name = raw_input()
age = raw_input()
kw = raw_input()

gain=person(name,age,**kw)

def func(a,b,c=0,*args,**kw):
    print 'a=',a, 'b=',b ,'c=',c, 'args=',args, 'kw=',kw

