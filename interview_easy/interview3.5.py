import math
print('\n')
print('For question3.5')
x=int(input('Enter number:'))

l = 1
y = math.ceil(x/2)
if x<=0:
	print('Enter number greater than zero')

for i in range(1,y+1):
	for k in range(i,y):
		print(' ',end='')
	print('*',end='')
	for j in range(l-2):
		print('*',end='')
	if i != 1:
		print("*", end='')
	l+=2
	print('')

if x%2 !=0:
	l = l - 2
for i in range(y,0,-1):
	if x%2 !=0:
		for k in range(i,y+1):
			print(' ',end='')
	else:
		for k in range(i,y):
			print(' ',end='')

	for j in range(l-2,0,-1):
		print("*", end='')
	l -= 2
	print('')
