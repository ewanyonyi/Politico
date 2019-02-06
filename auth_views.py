""" Admin REST api Views"""

from flask import Blueprint, request, make_response, jsonify
from develop.api.v1.models.auth_models import Users
from develop.api.v1.checkers.validators import Validator
AUTH_API_BLUEPRINT = Blueprint('auth', __name__)


@AUTH_API_BLUEPRINT.route('/api/v1/auth/signup', methods=['POST'])
def siginup():
    """ This method is used to register the user in the server using the REST api """
    # Get the post data
    post_data = request.get_json() # force=True to ignore header requirements
    settle_fields = Validator.validate_fields(post_data)
    settle_email = Validator.validate_email(post_data['email'])
    settle_password = Validator.validate_password(post_data['password'])
    settle_match_password = Validator.password_match(post_data['password'],post_data['confirm_password'])

    if not post_data:
        response_object = {
                "status":400,
                "error" : 'Bad Request'
            }
        return make_response(jsonify(response_object))

    elif settle_fields != True:
        response_object = {
            "status":400,
            "error" : settle_fields,
        }
        return make_response(jsonify(response_object))

    elif settle_email != True:
        response_object = {
            "status":400,
            "error" : settle_email
        }
        return make_response(jsonify(response_object))
    elif settle_password != True:
        response_object = {
            "status":400,
            "error" : settle_password
        }
        return make_response(jsonify(response_object))
    elif settle_match_password != True:
        response_object = {
            "status":400,
            "error" : settle_match_password
        }
        return make_response(jsonify(response_object))

    else:
        user = {
            'id':post_data['id'],
            'firstname':post_data['firstname'],
            'lastname':post_data['lastname'],
            'othername':post_data['othername'],
            'email':post_data['email'],
            'phoneNumber':post_data['phoneNumber'],
            'passportUrl':post_data['passportUrl'],
            'isAdmin':post_data['isAdmin'],
            'password':post_data['password'],
            'confirm_password':post_data['confirm_password']
        }
        Users.users_data.append(user)

        response_object = {
            'status': 201,
            'data':[
                {
                  'id':post_data['id'],
                  'firstname':post_data['firstname'],
                  'lastname':post_data['lastname'],
                  'othername':post_data['othername'],
                  'email':post_data['email'],
                  'phoneNumber':post_data['phoneNumber'],
                  'isAdmin':post_data['isAdmin'],
                  'password':'**********'
                }
           ]
        }
        return make_response(jsonify(response_object))

@AUTH_API_BLUEPRINT.route('/api/v1/auth/signin', methods=['POST'])
def siginin():
    """ This method is used to sigin in the user in the server using the REST api """
    # Get the post data
    post_data = request.get_json() # force=True to ignore header requirements

    if not post_data:
        response_object = {
                "status":400,
                "error" : 'Bad Request'
            }
        return make_response(jsonify(response_object))

    else:
        try:
            user = {
            'email':post_data['email'],
            'password':post_data['password']
            }
            for user in Users.users_data:
                email = post_data['email']
                if email == Users.users_data['email']:
                    response_object = {
                        'status': 200,
                        'data':[
                            {
                              'email':post_data['email'],
                              'password':'**********'
                            }
                        ]
                    }
                    return make_response(jsonify(response_object))
        except:
            response_object = {
                "status":404,
                "error" : 'User does not exist!'
            }
            return make_response(jsonify(response_object))
