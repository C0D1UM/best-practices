###############################################################################
# pattern 4
###############################################################################

# Get python version
import sys
version = int(sys.version[0])

# Get input
n = 0
try:
    if version == 3:
        n = int(input("enter number of layers(ctrl+c to quit): "))
    else:
        n = int(raw_input("enter number of layers(ctrl+c to quit): "))
except KeyboardInterrupt:
    print("\nbye")
    sys.exit()
except:
    print("invalid number")

# set m to ceiling of half of n
m = int(n/2)
if n/2 - int(n/2) > 0:
    m += 1

if n % 2 == 0:
# Handle even number of layers
    for i in range(m*2, 1, -2):
        this_layer = " "*int( (m - i/2) ) + "*" + " "*int( i-2 )
        if i != 1:
            this_layer += "*"
        print(this_layer)
    for i in range(2, (m+1)*2, 2):
        this_layer = " "*int( (m - i/2) ) + "*" + " "*int( i-2 )
        if i != 1:
            this_layer += "*"
        print(this_layer)
else:
# Handle odd number of layers
    for i in range(m*2, 1, -2):
        this_layer = " "*int( (m - i/2) ) + "*" + " "*int( i-3 )
        if i != 2:
            this_layer += "*"
        print(this_layer)
    for i in range(4, (m +1)*2, 2):
        this_layer = " "*int( (m - i/2) ) + "*" + " "*int( i-3 )
        if i != 2:
            this_layer += "*"
        print(this_layer)

