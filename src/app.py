import string
import random

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# bad security practice, but allow cross-origin resource sharing
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello world'


# @app.route('/users/<id>')
# def get_users(id):
#     if id:
#         for user in users['users_list']:
#             if user['id'] == id:
#                 return user
#
#         return ({})
#
#     return users


@app.route('/users/<id>', methods=['GET', 'DELETE'])
def user_by_id(id):
    if id:

        if id not in users['users_list']:
            resp = jsonify(success=False, message="User ID does not exist")
            resp.status_code = 404

            return resp

        if request.method == 'GET':
            user = users['users_list'].get(id)
            return user

        elif request.method == 'DELETE':

            user_dict = users['users_list'].pop(id)

            resp = jsonify(user_dict)
            resp.status_code = 200
            print(resp)
            return resp

    resp = jsonify(success=False)
    resp.status_code = 400
    return resp



@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':

        search_username = request.args.get('name')
        search_job = request.args.get('job')

        if search_username or search_job:
            filtered_users = {'users_list': {}}
            for user in users['users_list'].items():

                if (search_username is None or user[1].get('name') == search_username) and \
                        (search_job is None or user[1].get('job') == search_job):
                    filtered_users['users_list'].update({user[0]: user[1]})

            return filtered_users

        return users

    elif request.method == 'POST':
        userToAdd = request.get_json()

        user_id = None
        while user_id is None or user_id in users['users_list']:
            user_id = ""
            for i in range(3):
                user_id += random.choice(string.ascii_lowercase)

            for i in range(3):
                user_id += str(random.randint(0,9))

        userToAdd.update({'id': user_id})
        users['users_list'].update({user_id: userToAdd})

        resp = jsonify(userToAdd)
        resp.status_code = 201
        return resp


@app.route('/teapot')
def im_a_teapot():
    resp = jsonify("I'm a teapot")
    resp.status_code = 418

    return resp


users = {
    'users_list': {
        'xyz789': {
            'id': 'xyz789',
            'name': 'Charlie',
            'job': 'Janitor',
        },
        'abc123': {
            'id': 'abc123',
            'name': 'Mac',
            'job': 'Bouncer',
        },
        'ppp222': {
            'id': 'ppp222',
            'name': 'Mac',
            'job': 'Professor',
        },
        'yat999': {
            'id': 'yat999',
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        'zap555': {
            'id': 'zap555',
            'name': 'Dennis',
            'job': 'Bartender',
        }
    }
}
