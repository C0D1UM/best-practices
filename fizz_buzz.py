#1
for i in range(1,101):
    if i%3 == 0:
        print("fizz ",end='')
    if i%5 == 0:
        print("buzz ",end='')
    elif i%3 != 0 and i%5 != 0:
        print(i," ",end='')

print("")