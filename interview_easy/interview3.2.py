m=int(input('Enter number:'))
if m<=0:
	print('Enter number greater than zero')
for i in range(1,m+1):
	for k in range(i,m):
		print(' ',end='')
	for j in range(1,i+1):
		print('*',end='')
	print('')




