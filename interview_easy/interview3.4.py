import math
n=int(input('Enter number :'))
l=1
a=1
y = math.ceil(n/2)

if(n==0):
	print('Enter number greater than zero')

if n%2==0:
	for i in range (n,1,-2): 
		for k in range(l-1):
			print(' ',end='')
		print('*',end='')
		for j in range(1,i-1):
			print(' ',end='')
		if i!=0:
			print('*',end='')
		print('')
		l=l+1
	m=1
	for i in range(1,n+1,2):
		for k in range(l-2):
			print(' ',end='')
		print("*", end='')
		for j in range(1,(2*m)-1):
			print(' ',end='')        
		if i != 0:
			print("*", end='')
		m=m+1
		l=l-1
		print('')

if n%2!=0:
	for i in range(n,0,-2):
		for k in range(a-1):
			print(' ',end='')
		print('*',end='')
		for j in range(1,i-1):
			print(' ',end='')
		if i!=1:
			print('*',end='')
		print('')
		a=a+1

	p=1
	for i in range(2,n+1,2):
		for k in range(a-3):
			print(' ',end='')
		print("*", end='')
		for j in range(1,2*(p)):
			print(' ',end='')
		if i!=1:
			print("*", end='')
		p=p+1
		a=a-1
		print('')

