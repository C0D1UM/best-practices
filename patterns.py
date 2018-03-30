#3.1
n = int(input("Enter the value of n:"))

for i in range(1,n+1):
    for j in range(i):
        print("*",end='')    
    print("")

#3.2
n = int(input("Enter the value of n:"))

for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end='')    
    for k in range(i):
        print("*",end='')
    print("")    

#3.3
n = int(input("Enter the value of n:"))

for i in range(n):  
    for j in range(n-1,i,-1):
        print(" ",end='')
    print("*",end='')
    for j in range(i+(i-1)):
        print(" ",end='')
    if i >= 1:
        print("*")
    elif i == 0:
        print("")        

#3.4
n = int(input("Enter the value of n:"))

i=0
reverse = False

while(i >= 0):
    if n == 1:
        print("*")
        break

    for j in range(i):
        print(" ",end='')
    print("*",end='')
    for k in range(n-2-2*i):
        print(" " if n>2 else '',end='')
    print("*" if i == 0 or i != int(n/2)  else '',end='')
    
    print("")
    
    if(not reverse):
        i += 1  
    elif(reverse):
        i -= 1
    
    if n%2 == 0 and i == n/2 and not reverse:
        i -= 1
        reverse = True
    elif i == int(n/2) and not reverse:
        reverse = True


n = int(input("Enter the value of n:"))

i=0
reverse = False

while(i >= 0):
    if n == 1:
        print("*")
        break
        
    for j in range(n-1,i-1,-1):
        print(" ",end='')
    for k in range(2*i+1):
        print("*",end='')    
    print("")
    
    if(not reverse):
        i += 1  
    elif(reverse):
        i -= 1
    
    if n%2 == 0 and i == n/2 and not reverse:
        i -= 1
        reverse = True
    elif i == int(n/2) and not reverse:
        reverse = True

n = int(input("Enter the value of n:"))

i=0
reverse = False

while(i >= 0):
    for j in range(n-2,i-1,-1):
        if not reverse:
            print("A",end='')
        else:
            print("C",end='')
    print("+",end='')            
    for k in range(2*(i-1)+1):
        print("E",end='')    

    print("+" if i > 0 else "",end='')
    
    for j in range(n-2,i-1,-1):
        if not reverse:
            print("B",end='')
        else:
            print("D",end='')

    print("")
    if(not reverse):
        i += 1  
    elif(reverse):
        i -= 1
    
    if i > n-1:
        i = n - 2
        reverse = True


#4
# the difference between else and finally is that else clause 
# executes if the try block doesn't run into any exception
# where as finally clause while coming out of the try block.

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("The result:",result)
    finally:
        print("Finally clause")

divide(2,1)
divide(2,0)
divide("2","1")