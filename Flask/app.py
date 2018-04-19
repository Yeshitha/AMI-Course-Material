from flask import Flask

app = Flask(__name__)

#Definition of one webpage
@app.route('/')         #URL address in the server
def hello_world():      #Define function which returns string that is actual conent of the string
    return 'Hello World!'  #Return string is whats shown to the user

#file favicon.ico if the icon of the webpage 404 NOT FOUND
#200 Everything is okay

if __name__ == '__main__':
    app.run()

#locally, only a browser on this computer can access the website
#Pubic, use a public interface
#Example 0.0.0.0 - Public web
#or use  port = 80(standarad)
#secnd choice if 80 not free use 8080
#check firewall if it doesnt block 8080
#safest way to go public use WSGI server to make it safe

