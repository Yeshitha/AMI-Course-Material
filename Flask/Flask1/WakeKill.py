from flask import Flask, render_template, url_for



app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index.html')
def index():      #Define function which returns string that is actual conent of the string
    return render_template("index.html")

@app.route('/about.html')
def about():
    url_for('index')
    return render_template("about.html")

if __name__ == '__main__':
    app.run()

#Static file that never change
