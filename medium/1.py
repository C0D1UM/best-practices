######################################################################
# Prime Numbers
######################################################################

# Get python version
import sys
version = int(sys.version[0])

# Get input
l = 0
try:
    if version == 3:
        l = int(input("enter limit: "))
    else:
        l = int(raw_input("enter limit: "))
except KeyboardInterrupt:
    print("\nbye")
    sys.exit()
except:
    print("invalid number")

primes = []
for i in range(2,l+1):
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)
print("%d -> %s" % (l, " ".join(map(str, primes)) ))
