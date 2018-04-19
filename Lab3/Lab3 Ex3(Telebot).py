#from telegram.ext import Updater

token = '573598791:AAF6kiGBOCp5Pc7cMsc1273bKVtjXT5R8sU' #Telegram Token

task = []

print('Welcome!')
print('todomanager')

def download(path):
    # 'C:\Users\yeshi\Dropbox\Polito\Third Year\Second Semester\Ambient Intelligence\Python Labs\course-materials\Lab2'
    print(path)
    file = open(path, 'r')
    task.extend(file.readlines())
    file.close()

def upload(path):
    print('Enter the name of the output file:')
    file = open(path, 'w')
    if len(task) == 0:
        print('List is empty!')
    else:
        for i in task:
            file.write(i)
    file.close()

def intial():
    print('1. Insert a new task')
    print('2. Remove a task')
    print('3. Show all existing tasks')
    print('4. Close program')
    print('Enter the number of the corresponding function:')

def new_task():
    print('Enter the name of the new task:')
    item = str(input())
    task.append(item)

def remove_task():
    print('Which task would you like to remove:')
    item = str(input())

    task_to_remove = []
    for i in task:
        if item in i:
            task_to_remove.append(i)

    for g in task_to_remove:
        if g in task:
            task.remove(g)

def show():
    if len(task) != 0:
        print(task)
    else:
        print('The list is empty!')

print('Please enter the name of the file which contains the tasks:')
name = str(input())
download(name)
intial()

while True:
    x = str(input())
    if x == '/showTasks':
        new_task()
        print('Please enter a number:')
    elif x == '/newTask':
        remove_task()
        print('Please enter a number:')
    elif x == '/removeTask':
        show()
        print('Please enter a number:')
    elif x == '/removeAllTasks':
        print('The program will terminate now')
        upload(name)
        break
    else:
        print('Please enter a number between 1 and 4')