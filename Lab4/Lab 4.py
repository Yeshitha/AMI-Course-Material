import pymysql



if __name__ == '__main__':
    connection = pymysql.connect(user = 'root', password = 'root', host = 'localhost', database = 'todolist')

    sql1 = "select * from todo"

    cursor = connection.cursor()
    cursor.excute(sql1)

    result = cursor.fetchall()

    for i in result:
        print(i)

    cursor.close()

