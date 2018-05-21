from flask import Flask, redirect, url_for, jsonify


task1 = {'task_number':'1','name':'Wash the car','urgent':'No'}
task2 = {'task_number':'2','name':'Buy food','urgent':'Yes'}
task3 = {'task_number':'3','name':'Find happiness!','urgent':'Yes'}

task = [task1, task2, task3]

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/tasks')
def show_tasks():
    return jsonify(task)


@app.route('/tasks/<task_number>')
def find(task_number):
    found
    if len(found) == 1:
        return jsonify(found)
    esle:
        response = jsonify({ 'message': "Invalid user "+name })
        response.status_code = 404
        return response



if __name__ == '__main__':
    app.run()
