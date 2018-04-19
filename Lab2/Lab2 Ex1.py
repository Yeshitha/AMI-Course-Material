task = []

print('Welcome!')
print('todomanager')

def intial():
    print('1. Insert a new task')
    print('2. Remove a task')
    print('3. Show all existing tasks')
    print('4. Close program')

def new_task():
    print('Enter the name of the new task:')
    item = str(input())
    task.append(item)

def remove_task():
    print('Which task would you like to remove:')
    item = str(input())
    task.remove(item)

def show():
    task.sort()
    if len(task) != 0:
        print(task)
    else:
        print('The list is empty!')

intial()

while True:
    print('Enter the number of the corresponding function:')
    x = int(input())
    if x == 1:
        new_task()
        print('Please enter a number:')
    elif x == 2:
        remove_task()
        print('Please enter a number:')
    elif x == 3:
        show()
        print('Please enter a number:')
    elif x == 4:
        print('The program will terminate now')
        break
    else:
        print('Please enter a number between 1 and 4')