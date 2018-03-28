###############################################################################
# pattern 6
###############################################################################

# Get python version
import sys
version = int(sys.version[0])

# Get input
n = 0
try:
    if version == 3:
        n = int(input("enter n(ctrl+c to quit): "))
    else:
        n = int(raw_input("enter n(ctrl+c to quit): "))
except KeyboardInterrupt:
    print("\nbye")
    sys.exit()
except:
    print("invalid number")

# Print the top half.
for i in range(1,(n)*2,2):
    this_layer =  "A"*int( (n - i/2) ) 
    this_layer += "+" + "E"*int( i-2 ) 
    if i != 1:
        this_layer += "+"
    this_layer += "B"*int( (n - i/2) )
    print(this_layer)

# Print the bottom half.
for i in range((n)*2-2,1,-2):
    this_layer =  "C"*int( (n - i/2) ) 
    this_layer += "+" 
    this_layer += "E"*int(i-3) 
    if i-3 != -1:
        this_layer += "+"
    this_layer += "D"*int( (n - i/2) )
    print(this_layer)
