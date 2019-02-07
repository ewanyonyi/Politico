""" Admin REST api Views"""

from flask import Blueprint, request, make_response, jsonify
from develop.api.v1.auth.auth_models import Users, users_data
from develop.api.v1.checkers.validators import Validator
AUTH_API_BLUEPRINT = Blueprint('auth', __name__)


@AUTH_API_BLUEPRINT.route('/auth/signup', methods=['POST'])
def siginup():
    """ This method is used to register the user in the server using the REST api """
    # Get the post data
    post_data = request.get_json(force=True) # force=True to ignore header requirements
    settle_email = Validator.validate_email(post_data['email'])
    settle_password = Validator.validate_password(post_data['password'])

    if not post_data:
        response_object = {
            "status":400,
            "error" : 'Bad Request'
        }
    elif post_data is None:
        response_object = {
            "status":400,
            "error" : 'Bad Request'
        }
    
    elif settle_email != 1:
        response_object = {
            "status":400,
            "error" : settle_email
        }
    elif settle_password != 1:
        response_object = {
            "status":400,
            "error" : settle_password
        }
    else:
        user = Users(
            id=post_data.get('id'),
            firstname=post_data.get('firstname'),
            lastname=post_data.get('lastname'),
            othername=post_data.get('othername'),
            email=post_data.get('email'),
            phone_number=post_data.get('phone_number'),
            passport_url=post_data.get('passport_url'),
            is_admin=post_data.get('isAdmin'),
            password=post_data.get('password')
        )
        user.save()

        response_object = {
            'status': 201,
            'data':[
                {
                    'messege':'Successfully registered.'
                }
            ]
        }
    return make_response(jsonify(response_object))

@AUTH_API_BLUEPRINT.route('/auth/signin', methods=['POST'])
def siginin():
    """ This method is used to sigin in the user in the server using the REST api """
    # Get the post data
    post_data = request.get_json(force=True) # force=True to ignore header requirements
    email = post_data.get('email')
    password = post_data.get('password')
    if post_data is None:
        response_object = {
            "status":400,
            "error" : 'Bad Request'
        }
    else:
        for user in users_data:
            if user.get('email') == email and user.get('password') == password:
                response_object = {
                    'status': 200,
                    'data':[
                        {
                            'message':'Successfully logged in.'
                        }
                    ]
                }
    return make_response(jsonify(response_object))    
