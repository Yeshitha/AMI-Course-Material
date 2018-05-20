from flask import Flask, redirect, render_template, request


task = ['cats', 'dogs', 'birds', 'bees']

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect("/index.html")


@app.route('/index.html')
def index():
    return render_template('index.html', value=task)


@app.route('/insertpage.html')
def insertpage():
    task = request.form()
    return render_template('insertpage.html')


if __name__ == '__main__':
    app.run()
