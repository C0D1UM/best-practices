import math


def is_prime(data):
    data = int(data)
    prime = 0
    if data == 1 or data == 0:
        prime = 1
    else:
        for x in range(2, int(math.sqrt(data)+1)):
            if (data % x == 0):
                prime = 1
                break
    if prime == 1:
        return False
    else:
        return True


if __name__ == "__main__":
  n = int(input())
  for i in range(n):
    if is_prime(i):
      print(i)