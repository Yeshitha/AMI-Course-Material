from flask import Flask, redirect, render_template, request


tasks = ['cats', 'dogs', 'birds', 'bees', 'Submit']

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
        task = str(request.form['task'])
        tasks.append(task)
        return render_template('insert_task.html', value=tasks)
    return render_template('index.html', value=tasks)


@app.route('/delete_task.html', methods=['POST', 'GET'])
def delete_task():
    if request.method == 'POST':
        task = str(request.form['Remove'])
        print(task)
        tasks.remove(task)
        return render_template('delete_task.html', value=tasks)
    return render_template('index.html', value=tasks)


if __name__ == '__main__':
    app.run()
