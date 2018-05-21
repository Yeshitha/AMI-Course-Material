import requests

base_url = 'http://localhost:5000'

if __name__ == '__main__':
    #get list of users
    users = requests.get(base_url+'/users').json()
    print(users)


    for user in users:
        userinfo = requests.get(base_url+'/users/'+user['name']).json
        print(userinfo)


    #adding a new usera
    new_user = [ 'name':'AE', 'firstname': 'Albert', 'lastname': 'Einstein']

    requests.post(base_url+'/users', json=new_user)