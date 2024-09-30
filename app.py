from modules.helper_functions.user import User
from modules.user_action import user_action
from modules.accounts_handler import accounts
from flask import Flask, jsonify, request, Response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from logger import logger
import logging
import traceback


app = Flask(__name__)
auth = HTTPBasicAuth()

# setting up logger and a file handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler = logging.FileHandler("app.log")
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)


@auth.verify_password
def verify_password(username, password):
    acc_lst = accounts.get_accounts()
    if username in acc_lst and \
            check_password_hash(acc_lst.get(username), generate_password_hash(password)):
        return username


#endpoint to get all users
@auth.login_required
@app.route('/', methods=['GET'])
def get_users():
    return jsonify(user_action.get_users())


#endpoint to add user
@auth.login_required
@app.route('/', methods=['POST'])
def create_user():
    if request.get_data() != b'' and 'email' in request.get_json() and 'password' in request.get_json():
        user = User(request.json['email'], request.json['password'])
        return user_action.add_user(user)
    else:
        return "please enter all user info", 422


#endpoint to update user password
@auth.login_required
@app.route('/', methods=['PUT'])
def update_user():
    if request.get_data() == b'' or 'email' not in request.get_json() or 'password' not in request.get_json():
        return "please enter all user info", 422
    user = User(request.json['email'], request.json['password'])
    if 'new_password' not in request.get_json():
        return "please add new password", 422
    else:
        new_pass = request.json['new_password']
        return user_action.update_user(user, new_pass)


#endpoint to delete user
@auth.login_required
@app.route('/', methods=['DELETE'])
def delete_user():
    if request.get_data() != b'' and 'email' in request.get_json() and 'password' in request.get_json():
        user = User(request.json['email'], request.json['password'])
        return user_action.delete_user(user)
    else:
        return "please enter all user info", 422


@app.after_request
def after_request(response):
    logger.info('%s %s %s %s %s', request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response


@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', request.remote_addr, request.method, request.scheme, request.full_path, tb)
    return e


if __name__ == '__main__':
    app.run(port=5000)

