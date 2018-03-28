###############################################################################
# pattern 2
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

# Print pattern
for i in range(1,n+1):
    print(" "*(n - i) + "*" * i)
