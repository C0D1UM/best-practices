import os
import redis

r = redis.Redis()
name = 'task'


def enter_task():
    print('----------------------------------------------')
    print('Stop entering task by entering a blank task')
    print('----------------------------------------------')
    while True:
        task_name = input('> Enter a chore or task: ')
        if task_name != '':
            with open('task.txt', 'a') as file:
                file.write(task_name + '\n')
                r.rpush(name, task_name)
        else:
            break


def display_task():
    with open('task.txt', 'r') as file:
        tasks = file.read()
        print('----------------------------------------------')
        print(' List of all the task')
        print('----------------------------------------------')
        task_id = 1
        if os.stat('task.txt').st_size != 0:
            for task in tasks.split('\n'):
                if task:
                    print(f'{task_id} {task}')
                    task_id += 1
        else:
            print('There is no task list!')
            print('----------------------------------------------')


def remove_task():
    print('----------------------------------------------')
    print('Stop remove a task by entering a blank task id')
    print('----------------------------------------------')
    while True:
        if os.stat('task.txt').st_size != 0:
            task_id = input('> Remove a task id: ')
            if task_id != '':
                with open('task.txt', 'r') as file:
                    tasks = file.readlines()
                line = 1
                r.flushall()
                with open('task.txt', 'w') as file:
                    for task in tasks:
                        if line == int(task_id):
                            pass
                        else:
                            file.write(task)
                            task = task.strip()
                            r.rpush(name, task)
                        line += 1
                with open('task.txt', 'r') as file:
                    tasks = file.read()
                    print('----------------------------------------------')
                    print('List of all the task')
                    print('----------------------------------------------')
                    task_id = 1
                    if os.stat('task.txt').st_size != 0:
                        for task in tasks.split('\n'):
                            if task:
                                print(f'{task_id} {task}')
                                task_id += 1
                        print('----------------------------------------------')
                    else:
                        print('There is no task list!')
                        print('----------------------------------------------')
                        print('> Process finished')
                        break
            else:
                print('> Process finished')
                break
        else:
            print('> Process finished')
            break


def main():
    enter_task()
    display_task()
    remove_task()


if __name__ == '__main__':
    main()
