import models

from flask import Blueprint, jsonify, request
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

#register our user blueprint
#pass in the blueprint name and the import_name

user = Blueprint('users', 'user')



@user.route('/register', methods=["POST"])
def register():
    ## see request payload anagolous to req.body in express
    ## This is how you get the image you sent over


    ## This has all the data like username, email, password
    payload = request.get_json()



    payload['email'].lower()
    try:
        # Find if the user already exists?
        models.User.get(models.User.email == payload['email']) # model query finding by email
        return jsonify(data={}, status={"code": 401, "message": "A user with that name already exists"})
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password']) # bcrypt line for generating the hash
        user = models.User.create(**payload) # put the user in the database
                                             # **payload, is spreading like js (...) the properties of the payload object out

        #login_user
        login_user(user) # starts session

        user_dict = model_to_dict(user)
        print(user_dict)
        print(type(user_dict))
        # delete the password
        del user_dict['password'] # delete the password before we return it, because we don't need the client to be aware of it

        return jsonify(data=user_dict, status={"code": 201, "message": "Success"})



@user.route('/login', methods=["POST"])
def login():
    payload = request.get_json()
    print(payload, '< --- this is playload')
    try:
        user = models.User.get(models.User.email== payload['email'])
        user_dict = model_to_dict(user)
        if(check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)
            print(user, ' this is user')
            return jsonify(data=user_dict, status={"code": 200, "message": "Success"})
        else:
            return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})




# @user.route('/register', method=['POST'])
# def register():
#     """Accepts a post request with new user's email and password"""
#     payload = request.get_json()

#     if not payload['email'] or not payload['password']:
#         return jsonify(status=400)

# #make sure we handle
# # username?email has not been use before
# # passwod match

#     try:
#     # won't throw an exception if email already in db
#         model.User.get(models.User.email ** payload['email'])
#         return jsonify(data={}, status={'code':400, 'message': 'A user with that email alredy exist.'})
#     except models.DoesNotExist:
#         payload['password'] = generate_password_hash(payload['password'])
#         user = models.user.create(**payload)
#         profile = models.Profile.create(user=user)


#     # start new session with new user
#         login_user(user)

#         user_dict = model_to_dict(user)
#         print(user_dict)
#         print(type(user_dict))

#     # delete password before sending user dict back to the client

#         del user_dict['password']

#         return jsonify(data=user_dict, status={'code':201, 'message': 'User created'})


# @user.route('/login', methods=['POST'])
# def login():
#     """Route to log user by compare pw hash from db to hashed pw attempt send from the client"""
#     payload = request.get_json()

#     try:
#         user = models.User.get(models.User.email ** payload['email'])
#         user_dict = model_to_dict(user)

#         if(check_passwod_hash(user_dict['password'], payload['password'])):
#            del user_dict['password']
#            login_user(user)
#            print('User is:', user)
#            return jsonify(data=user_dict, status={'code':200, 'message': 'User authenticated'})

#         return jsonify(data={}, status={'code':401, 'message': 'Email or password is incorrect'})

#     except models.DoesNotExist:
#         return jsonify(data={}, status={'code':401, 'message': 'Email or password is incorrect'})









