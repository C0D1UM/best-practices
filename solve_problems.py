# Interview Problems


# Easy - Problem 1
def fizz_buzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz', end=' ')
        elif num % 3 == 0:
            print('Fizz', end=' ')
        elif num % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(num, end=' ')
        if num % 20 == 0:
            print('\n', end='')


fizz_buzz()


# Easy - Problem 2
def leap_year(year):
    if year % 400 == 0:
        print(f'{year} -> true')
    elif year % 400 != 0 and year % 100 != 0 and year % 4 == 0:
        print(f'{year} -> true')
    else:
        print(f'{year} -> false')


leap_year(1600)
leap_year(2000)
leap_year(1500)
leap_year(2004)
leap_year(2008)
leap_year(2010)


# Easy - Problem 3.1
def star_pattern1(n):
    for i in range(n):
        print('' * (n - i - 1) + '*' * (i + 1))


print('n=3')
star_pattern1(3)
print('n=4')
star_pattern1(4)
print('n=6')
star_pattern1(6)


# Easy - Problem 3.2
def star_pattern2(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (i + 1))


print('n=3')
star_pattern2(3)
print('n=4')
star_pattern2(4)
print('n=6')
star_pattern2(6)


# Easy - Problem 3.3
def star_pattern3(n):
    for i in range(n):
        for j in range(2 * n - 1):
            if i + j == n - 1 or j - i == n - 1:
                print('*', end='')
            else:
                print(end=' ')
        print()


print('n=1')
star_pattern3(1)
print('n=2')
star_pattern3(2)
print('n=3')
star_pattern3(3)
print('n=4')
star_pattern3(4)
print('n=5')
star_pattern3(5)


# Easy - Problem 3.4
def star_pattern4(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print('*', end='')
            else:
                print(end=' ')
        print()


print('n=1')
star_pattern4(1)
print('n=2')
star_pattern4(2)
print('n=3')
star_pattern4(3)
print('n=4')
star_pattern4(4)
print('n=5')
star_pattern4(5)


# Easy - Problem 3.5
def star_pattern5(n):
    for i in range(n):
        if i < n / 2:
            print(' ' * (n // 2 - i), end='')
            print('*' * (i * 2 + 1))
        else:
            print(' ' * (n // 2 - n + i + 1), end='')
            print('*' * ((n - i) * 2 - 1))


print('n=1')
star_pattern5(1)
print('n=2')
star_pattern5(2)
print('n=3')
star_pattern5(3)
print('n=4')
star_pattern5(4)
print('n=5')
star_pattern5(5)
print('n=9')
star_pattern5(9)


# Easy - Problem 3.6
def character_pattern(n):
    j = 2 * n - 1
    for i in range(j):
        if i < j / 2:
            print('A' * (j // 2 - i), end='')
            print('+', end='')
            print('E' * (i * 2 - 1), end='')
            if i > 0:
                print('+', end='')
            print('B' * (j // 2 - i))
        else:
            print('C' * (j // 2 - j + i + 1), end='')
            print('+', end='')
            print('E' * (2 * j - 2 * i - 3), end='')
            if i < j - 1:
                print('+', end='')
            print('D' * (j // 2 - j + i + 1))


print('n=1')
character_pattern(1)
print('n=2')
character_pattern(2)
print('n=3')
character_pattern(3)
print('n=4')
character_pattern(4)


# Easy - Problem 4
""" 
else

If there is no exception raised in the try section, the else code is executed. 
This block's code is identical to regular code. If an exception is thrown, 
this block will not execute and the program may be terminated. 

finally

This code runs last, after all other blocks have finished running; 
it will run even if there was no exception or an uncaught exception, 
or if any of the other blocks above have a return statement; 
it will run in every instance.
"""


# Medium - Problem 1
def prime_numbers(n):
    print(f'{n} -> ', end='')
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            print(num, end=' ')


prime_numbers(20)
