###############################################################################
# Leap Year
###############################################################################

import sys
version = int(sys.version[0])
while True:
    try:
        if version == 3:
            year = int(input("enter year(ctrl+c to quit): "))
        else:
            year = int(raw_input("enter year(ctrl+c to quit): "))
    except KeyboardInterrupt:
        print("\nbye")
        sys.exit()
    except:
        print("invalid date")
        continue
    if ( year % 400 == 0 ) or ( year % 100 != 0 and year % 4 == 0 ):
        print("%d -> true" % year)
    else:
        print("%d -> false" % year)
