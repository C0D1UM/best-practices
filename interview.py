# Todo_list
# Make sure Redis is installed: python -m easy_install redis
import redis


def todo_list():
    conn = redis.Redis()
    repo = 'tasks'
    intro = "Hello! Enter as many tasks as you'd like, and press enter twice when you're finished."
    print(intro)
    try:
        with open("tasks.txt", "r+") as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        f = open("tasks.txt", "w+")
        tasks = f.read().splitlines()
        f.close()
    while True:
        my_task = input("Task: ")
        if my_task == '':
            break
        tasks.append(my_task)
    while True:
        item_id = 1
        print("These are your tasks")
        if tasks.__sizeof__() == 0:
            print("No tasks remaining")
        for item in tasks:
            print(f"{item_id}: {item}")
            item_id += 1
        print("Enter the number of a task you would like to delete or 'q' to quit.")
        choice = input("> ")
        if choice == 'q' or choice == '' or choice == '0':
            break
        try:
            number = int(choice) - 1
            try:
                conn.srem(repo, tasks[number])
            except:
                print('Could not connect to a Redis instance')
            tasks.pop(number)
        except IndexError:
            print("That is not a valid number")
        except ValueError:
            print("You must enter a number or 'q' to quit.")
    item_id = 1
    print("These are your remaining tasks")
    f = open("tasks.txt", "w+")
    for task in tasks:
        f.write(f"{task}\n")
        try:
            conn.sadd(repo, task)  # Add task to a set in Redis
        except:
            print('Could not connect to a Redis instance')
        print(f"{item_id}: {task}")
        item_id += 1
    f.close()
    conn.close()


todo_list()

# Easy_exercises
# Exercise 1


def fizz():
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')


fizz()

# Exercise 2


def leap_year(e):
    if e % 400 == 0:
        print(f"{e} -> true")
    elif e % 4 == 0 and e % 100 != 0:
        print(f"{e} -> true")
    else:
        print(f"{e} -> false")


leap_year(1600)
leap_year(2000)
leap_year(1500)
leap_year(2004)
leap_year(2008)
leap_year(2010)

# Exercise 3.1


def star_one(e):
    for i in range(e):
        print('*' * (i + 1))


print('n=3')
star_one(3)
print('n=4')
star_one(4)
print('n=6')
star_one(6)

# Exercise 3.2


def star_two(e):
    for i in range(e):
        print(' '*(e-i-1), end='')
        print('*' * (i + 1))


print('n=3')
star_two(3)
print('n=4')
star_two(4)
print('n=6')
star_two(6)

# Exercose 3.3


def star_three(e):
    print(' ' * (e-1), end='')
    print('*', end='')
    print(' ' * (e-1))
    for i in range(e-1):
        print(' '*(e-i-2), end='')
        print('*', end='')
        print(' '*(i*2+1), end='')
        print('*')


print('n=1')
star_three(1)
print('n=2')
star_three(2)
print('n=3')
star_three(3)
print('n=4')
star_three(4)
print('n=5')
star_three(5)

# Exercise 3.4


def star_four(e):
    for i in range(e):
        if i < e//2:
            print(' ' * i, end='')
            print('*', end='')
            print(' ' * (e - i * 2 - 2), end='')
            print('*')
        elif i == e//2 and e % 2 != 0:
            print(' ' * i, end='')
            print('*')
        else:
            print(' ' * (e - i - 1), end='')
            print('*', end='')
            print(' ' * (i * 2 - e), end='')
            print('*')


print('n=1')
star_four(1)
print('n=2')
star_four(2)
print('n=3')
star_four(3)
print('n=4')
star_four(4)
print('n=5')
star_four(5)

# Exercise 3.5


def star_five(e):
    for i in range(e):
        if i < e/2:
            print(' ' * (e // 2 - i), end='')
            print('*' * (i * 2 + 1))
        else:
            print(' ' * (e // 2 - e + i + 1), end='')
            print('*' * ((e - i - 1) * 2 + 1))


print('n=1')
star_five(1)
print('n=2')
star_five(2)
print('n=3')
star_five(3)
print('n=4')
star_five(4)
print('n=5')
star_five(5)
print('n=9')
star_five(9)

# Exercise 3.6


def star_six(e):
    r = 2 * e - 1
    for i in range(r):
        if i < r / 2:
            print('A' * (r // 2 - i), end='')
            print('+', end='')
            print('E' * (i * 2 - 1), end='')
            if i > 0:
                print('+', end='')
            print('B' * (r // 2 - i))
        else:
            print('C' * (r // 2 - r + i + 1), end='')
            print('+', end='')
            print('E' * (2 * r - 2 * i - 3), end='')
            if i < r - 1:
                print('+', end='')
            print('D' * (r // 2 - r + i + 1))


print('n=1')
star_six(1)
print('n=2')
star_six(2)
print('n=3')
star_six(3)
print('n=4')
star_six(4)


# Exercise 4
# The 'finally' block in exception handling is
# meant for a code block that has to be executed
# regardless if any exception (handled by any
# except block or not) gets thrown or not.

# The 'else' block in exception handling is a block
# of code that will only be executed if the tried
# statement does NOT throw an exception.

# Exceptions thrown in both code blocks will not
# be handled by the except block.

# Medium_exercises
# Exercise 1


def find_primes(e):
    for i in range(e+1):
        if i > 1:
            found_division = False
            for j in range(2, i):
                if i % j == 0:
                    found_division = True
            if not found_division:
                print(i, end=' ')


find_primes(20)
