if __name__ == '__main__':
    for i in range(100):
      number = i+1
      if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
      elif number % 3 == 0:
        print("Fizz")
      elif number % 5 == 0:
        print("Buzz")
      else:
        print(number)