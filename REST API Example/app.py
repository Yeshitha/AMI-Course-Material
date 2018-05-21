from flask import Flask, jsonify, request

app = Flask(__name__)

user1 = { 'name':'FC','firstname':'Fulvio', 'lastname':'Corno'}
user2 = { 'name':'LDR','firstname':'Luigi', 'lastname':'De Rusiis'}

users = [ user1, user2 ]

"""

Resources = user -> /users/FC -> Get(GET) 
Collection = user -> /users ->List (GET), Create (POST)

"""

@app.route('/users')
def ListUsers():
    #get list of object into python variable
    usernames = [ user['name'] for user in users ]
    return jsonify(usernames)

@app.route('/users/<name>')
def GetUsers(name):
    user = [ user for user in users if user['name'] == name ]
    if len(user) == 1:
        return jsonify(user[0])
    else:
        response = jsonify([ 'message': 'user not found: '+name ])
        response.status_code = 404
        return response


@app.route('/user', methods=['POST'])
def CreateUsers():
    new_user = request.json
    #new_user has to represent a user
    #new_user can't be already in the collection
    users.append(new_user)
    return jsonify(new_user)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
