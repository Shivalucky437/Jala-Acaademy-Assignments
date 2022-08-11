print('welcome to python basics assignment')
print()
name=input('enter your name ')
print()
print('have a great Learning',name)
print()

# '#' is used for single line comment

''' triple quotes is used for
    multiline comments'''
'it is also acts as a comment until we assign it to a variable'

n=input('enter a num ')
#n is a str type
print('{} is a '.format(n),type(n),' type')
print('value in str is "{} " '.format(n)+" or '{}' ".format(n))

#convertiny str to int
n=int(n)
print()
print('str to int conversion :')
print()
print('{} is a '.format(n),type(n),' type')
print('value in int is',n)
print()

print('str to float conversion :')
print()
m=float(n)
print('{} is a '.format(n),type(m),' type')
print('{} value in float is'.format(n),m)

print()
m=bool(n)
print('str to bool converaion :')
print('{} is a '.format(str(n)),type(m),' type')
print('{} value in bool is'.format(n),m)

#NOTE: char and double is not present kn python

print()
n='im a global var'
def scopeofvar():
	n='im a local var'
	print(n)
print(n)
#only global var is responding

'''for local variable access we have to call the function '''

s=scopeofvar()

