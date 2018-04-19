todo = []

def print_list():
    tasks = ['1. insert a new task', '2. remove a task', '3. show all existing tasks', '4. close the program']
    for i in tasks:
        print(i)

def insert():
    print('The name of the task you would like to enter into the list?')
    new_task = input()
    todo.append(new_task)

def remove():
    print('Enter the task you want to remove?')
    y = str(input())
    todo.remove(y)

def show():
    if len(todo) == 0:
        print('The list is empty!')
    else:
        print(todo)

print('todo_manager')
print('Insert the number corresponding to the action you want to perform:')

print_list()
print('Please enter a number:')

while 1 == True:
    x = int(input())
    if x == 1:
        insert()
        print('Please enter a number:')
    elif x == 2:
        remove()
        print('Please enter a number:')
    elif x == 3:
        show()
        print('Please enter a number:')
    elif x == 4:
        print('Program will terminate now')
        break
    else:
        print('Please enter a number between 1 and 4')

