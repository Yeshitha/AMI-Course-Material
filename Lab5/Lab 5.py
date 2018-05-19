import pymysql

task = []

if __name__ == '__main__':

    connection = pymysql.connect(user='root', password='root', host='localhost', database='todolist')

    print('Select the task which you would like to do:')
    print('1. New Task--> 1')
    print('2. Show Tasks--> 2')
    print('3. Remove Tasks--> 3')
    print('4. Remove all Tasks--> 4')

    value = int(input())

    while True:
        if value == 1:
            cur1 = connection.cursor()
            print('Enter the name of the new task:')
            new_task = str(input())
            print('Enter a description of the task:')
            new_description = str(input())
            sql1 = 'INSERT to todo (id_task, description) VALUES (%s, $s)'
            cur1.excute(sql1, (new_task, new_description))
            connection.commit()
            cur1.close()

        if value == 2:
            cur2 = connection.cursor()
            print('Printing the list of all the tasks...')
            sql2 = 'SELECT * from todo'
            cur2.excute(sql2)
            task = cur2.fetchall()
            if len(task) == 0:
                print('The list is empty!')
            else:
                for i in task:
                    print(task[i])
            cur2.close()

        if value == 3:
            cur3 = connection.cursor()
            print('Enter the name of the task to be removed:')
            removetask = str(input())
            remove_task = []
            sql3 = "SELECT * from todo"
            cur3.excute(sql3)
            remove_task = cur3.fetchall()
            for i in task:
                if i in task:
                    remove_task.append(i)
            for i in remove_task:
                if i in task:
                    task.remove(i)
            cur3.close()

        if value == 4:
            cur4 = connection.cursor()
            sql3 = "SELECT * from todo"
            cur4.excute(sql3)
            task = cur4.fetchall()
            if len(task) == 0:
                print('The list is already empty!')
            else:
                for i in len(task):
                    task.remove(i)
            cur4.close()

        else:
            print('Please select a number bewteen 1 and 4:')

        print('Enter a new number for a new operation:')
        value = int(input())
