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


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        if search_username:
            subdict = {'users_list': []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users

    elif request.method == 'POST' :
        userToAdd = request.get_json()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)

        return resp

users = {
    'users_list':
        [
            {
                'id': 'xyz789',
                'name': 'Charlie',
                'job': 'Janitor',
            },
            {
                'id': 'abc123',
                'name': 'Mac',
                'job': 'Bouncer',
            },
            {
                'id': 'ppp222',
                'name': 'Mac',
                'job': 'Professor',
            },
            {
                'id': 'yat999',
                'name': 'Dee',
                'job': 'Aspring actress',
            },
            {
                'id': 'zap555',
                'name': 'Dennis',
                'job': 'Bartender',
            }
        ]
}
