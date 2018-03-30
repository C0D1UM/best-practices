#leap year
n = int(input("Enter a number:"))
primes = []
prime = False

for i in range(n+1):
    if i == 2:
        primes.append(i)
    else:
        for j in range(2,i,1):
            if(i%j != 0):
                prime = True
                continue
            else:
                prime = False
                break    
        if prime:
            primes.append(i)

print(n," -> ",primes)