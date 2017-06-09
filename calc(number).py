def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum+n*n
	return sum

numbers=raw_input();
gain=calc(numbers)

print u'%d'  %(gain)

