from flask import Flask, request, jsonify

app = Flask(__name__)


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


@app.route('/users/<id>', methods=['GET'])
def get_user_by_id(id):
    if id:
        if request.method == 'GET':
            user = users['users_list'].get(id)
            if user is None:
                resp = jsonify(success=False, message="This user does not exist")
                resp.status_code = 404

                return resp

            return user

        else:
            resp = jsonify(success=False, message="Can only get a user by its ID")
            resp.status_code = 405

            return resp


@app.route('/users', methods=['GET', 'POST', 'DELETE'])
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
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)

        return resp

    elif request.method == 'DELETE':
        userToDelete = request.get_json()
        user_id = userToDelete.get('id')
        if user_id is not None:
            user_dict = users['users_list'].pop(user_id, None)

            if user_dict is None:
                resp = jsonify(success=False, message="User ID does not exist")
                resp.status_code = 404
            else:
                return user_dict


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
