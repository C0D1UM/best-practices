###############################################################################
# pyramid 5
###############################################################################

# Get python version.
import sys
version = int(sys.version[0])

# Get input.
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

# Set m to ceiling of half of n.
m = int(n/2)
if n/2 - int(n/2) > 0:
    m += 1

# Print top half.
for i in range(2, (m+1)*2, 2):
    this_layer = " "*int( (m - i/2) ) + "*"*int( i-2 )
    if i != 1:
        this_layer += "*"
    print(this_layer)

# Print bottom half.
if n % 2 == 0:
    l = 0
else:
    l = 2 # if odd, don't repeat the bottom line of top half
for i in range(m*2-l, 1, -2):
    this_layer = " "*int( (m - i/2) ) + "*"*int( i-2 )
    if i != 1:
        this_layer += "*"
    print(this_layer)
