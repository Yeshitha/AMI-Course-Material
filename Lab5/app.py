from flask import Flask, redirect, render_template, request


tasks = ['cats', 'dogs', 'birds', 'bees']
new_task = []


app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect("/index.html")


@app.route('/index.html')
def index():
    return render_template('index.html', value=tasks)


@app.route('/insert_task.html', methods=['POST', 'GET'])
def insert_task():
    if request.method == 'POST':
        task = request.form['task']
        new_task.extend(tasks)
        new_task.extend(task)
        return render_template('insert_task.html', value=new_task)
    return render_template('index.html', value=tasks)


@app.route('/delete_task.html')
def delete_task():
    return render_template('delete_task.html')


if __name__ == '__main__':
    app.run()
