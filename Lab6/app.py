from flask import Flask, jsonify, request, redirect, json


task1 = {'task_number': '1', 'name': 'Wash the car', 'urgent': 'No'}
task2 = {'task_number': '2', 'name': 'Buy food', 'urgent': 'Yes'}
task3 = {'task_number': '3', 'name': 'Find happiness!', 'urgent': 'Yes'}

task = [task1, task2, task3]

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect('/tasks')


# Show all the tasks! DONE
@app.route('/tasks')
def api_tasks():
    return jsonify(task)


# Remove a task! DONE
@app.route('/tasks/remove/<remove_id>')
def api_delete(remove_id):
    print(task)
    chore = [u for u in task if u['task_number'] == remove_id]
    if len(chore) == 1:
        print(chore)
        x = int(remove_id)
        del task[x-1]
        print(task)
        response = jsonify({'message': "ID of removed task: " + remove_id})
        response.status_code = 200
        return response
    else:
        response = jsonify({'message': "Task with ID "+remove_id+" doesn't exist!"})
        response.status_code = 404
        return response


# Find a task! DONE
@app.route('/tasks/find/<task_number>')
def api_find(task_number):
    chore2 = [u for u in task if u['task_number'] == task_number]
    if len(chore2) == 1:
        print(chore2)
        return jsonify(chore2)
    else:
        response = jsonify({'message': "Invalid task: "+task_number+", can't find it!"})
        response.status_code = 404
        return response


# Add a task! DONE
@app.route('/tasks/create', methods=['POST'])
def api_create_task():
    if request.headers['Content-Type'] == 'application/json':
        new_task = request.json
        task.append(new_task)
    else:
        response = jsonify({'message': "Invalid task request"})
        response.status_code = 404
        return response


# Updating a task!
@app.route()
def api_update():

    return

if __name__ == '__main__':
    app.run()
