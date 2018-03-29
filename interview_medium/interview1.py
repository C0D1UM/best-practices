print('for medium 1st question')
y=int(input('Enter number : '))
a=[]
if y<=0:
	print('Enter number greater than zero')
else:
	for i in range(2,y+1):
		for j in range(2,i):
			if (i % j) == 0:
				break
		else:
			a.append(i)
	print(y,'->',end=' ')
	for i in range(0, len(a)):
		print(a[i],end=' ')
	print()
