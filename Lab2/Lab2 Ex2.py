task = []

print('Welcome!')
print('todomanager')

def download(path):
    # 'C:\Users\yeshi\Dropbox\Polito\Third Year\Second Semester\Ambient Intelligence\Python Labs\course-materials\Lab2'
    print(path)
    file = open(path, 'r')
    task.extend(file.readlines())
    file.close()

def upload():
    print('Enter the name of the output file:')
    path = str(input())
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
    task.remove(item)

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
        upload()
        break
    else:
        print('Please enter a number between 1 and 4')
