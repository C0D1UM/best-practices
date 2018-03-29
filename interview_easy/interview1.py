for i in range(1,101):
	if (i%3==0 and i%5==0) :
		print('FizzBuzz',end=' ')
	elif i%5==0 :
		print('Buzz',end=' ')
	elif i%3==0 :
		print('Fizz',end=' ')
	else:
		print(i,end=' ') 

