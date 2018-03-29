import math
print('\n')
print('For question3.6')
x=int(input('Enter number:'))
l = 1
m=1
if x<=0:
	print('Enter number greater than zero')
else:
 
 for i in range(1,x+2):
        for k in range(i,x+1):
                print('A',end='')
        print("+", end='')
        for j in range(l-2):
                print('E',end='')
        if i != 1:
                print("+", end='')
        for o in range(i,x+1):
         print('B',end='')        

        l+=2
        print('')
 l = l - 4
 for i in range(x,0,-1):
        for k in range(i,x+1):
                print('A',end='')
        print("+", end='')
        for j in range(l-2):
                print('E',end='')
        if i != 1:
                print("+", end='')
        for o in range(i,x+1):
         print('B',end='')        

        l-=2
        print('')
