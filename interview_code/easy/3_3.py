if __name__ == '__main__':
  n= int(input())
  for i in range(n):
    for j in range(1,n-i):
      print(' ', end = '')
    for k in range(0,(n+1)-(n-i)):
      print('*', end = '')
    print('')