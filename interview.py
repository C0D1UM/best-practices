# interview_easy
# question 1
print("\n Question 1 \n")
for i in range (1,100):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 5 == 0:
		print("Buzz")
	elif i % 3 == 0:
		print("Fizz")
	else:
		print(i)



print("\n Question 2 \n")
yearString = input("Enter a year")
year = int(yearString)
if year % 400 == 0:
	print( year , " -> 'True'")
elif year % 4 ==0 and year % 400 != 0 and year % 100 != 0:
	print( year , " -> 'True'")
else:
	print( year , " -> 'False'")



print("\n Question 3.1 \n ")

numString = input("Enter a num")
num = int(numString)

for i in range(0,num):
	for j in range(0,i+1):
		print('*', end='')
	print("\r")

print("\n Question 3.2 \n ")
numString = input("Enter a num: ")
num = int(numString)
for i in range(0,num):
	 print(' '*(num-i-1) + '*'*(i+1))

print("\n Question 3.3\n ")
numString = input("Enter a num: ")
num = int(numString)
middle_part =1
for i in range(1,num+1):
	for j in range(i,num):
		print(' ',end='')
	print("*", end='')
	for j in range(middle_part-2):
		print(' ',end='') 
	if i != 1:
		print("*", end='')
	middle_part+=2
	print('\r')

print("\n Question 3.4\n ")
numString = input("Enter a num: ")
num = int(numString)
middle_part =1
space =1
if num%2 ==1:
	for i in range(num,0,-2):
		for k in range(middle_part-1):
			print(' ',end='')
		print('*',end='')
		for j in range(1,i-1):
			print(' ',end='')
		if i!=1:
			print('*',end='')
		print('\r')
		middle_part=middle_part+1
	for i in range(2,num+1,2):
		for k in range(middle_part-3):
			print(' ',end='')
		print("*", end='')
		for j in range(1,2*space):
			print(' ',end='')
		if i!=1:
			print("*", end='')
		space=space+1
		middle_part=middle_part-1
		print('\r')

elif num%2 == 0:
	for i in range(num,1,-2):
		for j in range(middle_part - 1):
			print(' ' ,end = '')
		print("*",end = '')
		for j in range(1,i-1):
			print(' ',end='')
		if i!=0:
			print("*",end ='')
		print('\r')
		middle_part +=1

	for i in range(1,num+1,2):
		m_s = 2 * space -1
		for k in range(middle_part-2):
			print(' ',end='')
		print("*", end='')
		for j in range(1,m_s):
			print(' ',end='')        
		if i != 0:
			print("*", end='')
		space=space+1
		middle_part=middle_part-1
		print(' ')

print("\n Question 3.5 \n ")
numString = input("Enter a num: ")
num = int(numString)
if num >=3:
	for i in range(1,num+1):
		if i%2 ==0:
			print(' ')
		else:
			print(' '*int(num-i/2) + '*'*(i))
	 
else:
	for i in range(1,num+1):
		print('*')

print("\n Question 3.6 \n ")
numString = input("Enter a num: ")
num = int(numString)
a = 1

if num ==1:
	print("+")
else:
	for i in range(1,num+2):
		for j in range(i,num+1):
			print('A',end='')
		print("+", end='')
		for j in range(a-2):
			print('E',end='')
		if i != 1:
			print("+", end='')
		for j in range(i,num+1):
			print('B',end='')        
		a +=2
		print('')
	a = a - 4
	for i in range(num,0,-1):
		for j in range(i,num+1):
			print('A',end='')
		print("+", end='')
		for j in range(a-2):
			print('E',end='')
		if i != 1:
			print("+", end='')
		for j in range(i,num+1):
			print('B',end='')        
		a-=2
		print('')


#interview_medium
print("\n Question 1 \n")

numString = input("Enter a num: ")
num = int(numString)
for i in range(2, num+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)


