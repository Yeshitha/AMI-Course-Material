from flask import Flask, redirect, render_template, request


task = ['cats', 'dogs', 'birds', 'bees']

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect("/index.html")


@app.route('/index.html')
def index():
    return render_template('index.html', value=task)


@app.route('/insert_task.html')
def insert_task():
    return render_template('insert_task.html', value=task)


@app.route('/delete_task.html')
def delete_task():
    return render_template('delete_task.html')


if __name__ == '__main__':
    app.run()
