x=int(input('Enter number:'))
l = 1
if x<=0:
	print('Enter number greater than zero')

for i in range(1,x+1):
	for k in range(i,x):
		print(' ',end='')
	print("*", end='')
	for j in range(l-2):
		print(' ',end='') 
	if i != 1:
		print("*", end='')
	l+=2
	print('')

