from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect("/index.html")


@app.route('/index.html')
def index():
    return render_template('/index.html')


if __name__ == '__main__':
    app.run()
