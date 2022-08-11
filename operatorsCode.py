#code for artimatic operations
a,b=5,6

#addition of a and b
print('addition of {} + {} ='.format(a,b),a+b)

print() #subtraction of a and b
print('subtraction of {} - {} ='.format(a,b),a-b)

print() #a multiply with b
print('multiplication of {} * {} ='.format(a,b),a*b)

print() #a divided with b
print('division of {} / {} ='.format(a,b),a/b)

print() #a to the power of b
print('pow of {} ** {} ='.format(a,b),a**b)

print() #integral part of a/b
print('floor division of {} // {} ='.format(a,b),a//b) 

print() #remainder of a / b
print('remainder of {} % {} ='.format(a,b),a%b) 

print()
temp=a
a+=1
print('increment of {}++   ='.format(temp),a)
temp,b=b,5
print()
print('decrement of {}--   ='.format(temp),b)

print()
print('equality check of {} == {} is '.format(a,b),a==b)

print()
print('not equality check of {} != {} is '.format(a,b),a!=b)


print()
print('greaterthan check of {} > {} is '.format(a,b),a>b)


print()
print('lessthan check of {} < {} is '.format(a,b),a<b)

print()
print('greaterthan or eqaulity check of {} >= {} '.format(a,b),a>=b)

print()
print('lessthan or equality check of {} <= {} is '.format(a,b),a<=b)

if a<b:
	print()
	print('smaller one is {}  and greater one is {}'.format(a,b))
else:
		print()
		print('smaller one is {}  and greater one is {}'.format(b,a))
	
