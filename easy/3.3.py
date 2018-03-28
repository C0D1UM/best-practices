###############################################################################
# pattern 3
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

# Print the pattern
for i in range(1,(n)*2,2):
    this_layer = " "*int( (n - i/2) ) + "*" + " "*int( i-2 )
    if i != 1:
        this_layer += "*"
    print(this_layer)

