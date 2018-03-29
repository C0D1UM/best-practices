n = int(input('Enter number:'))
if n<=0:
	print('Enter number greater than 0')
for i in range(1,n+1):
	for j in range(1,i+1):
		print('*',end='')
	print('')
