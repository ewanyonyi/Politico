from flask import Blueprint, request, make_response, jsonify
from server.api.v1.models.office import Offices, offices_data

office_api_v1_blueprint = Blueprint('office', __name__)

@office_api_v1_blueprint.route('/offices', methods=['POST'])
def createoffice():
    """ This method is used to create a political office by the web site admin """
    # Get the post party data
    post_data = request.get_json(force=True)
    if post_data is None:
        response_object = {
            "code":400,
            "error" : 'Bad Request'
        }
    else:
        office = {
            'office_type':post_data.get('office_type'),
            'name':post_data.get('name')
        }

        stored_office_names = [d.get('name') for d in offices_data]
        office_types = ['Federal', 'Legislative', 'State', 'Local Government']
        if post_data['name'] in stored_office_names:
            response_object = {
                "code":409,
                "error":"Office name already exist !"
            }
        elif post_data['office_type'] not in office_types:
            response_object = {
                "code":409,
                "error":{"Choose office type from":office_types}
            }
        else:
            Offices.save(office)
            response_object = {
                'code': 201,
                'office':[
                    { 
                        'id':offices_data.index(office),
                        'office_type':post_data['office_type'],
                        'name':post_data['name']
                    }
                ]
            }
    return make_response(jsonify(response_object), response_object.get('status'))

@office_api_v1_blueprint.route('/offices', methods=['GET'])
def getalloffices():
    """ This method is used to get all the political parties """
    # Get all the political offices
    response_object = {
        "code":200,
        "data":offices_data
    }
    return make_response(jsonify(response_object), 200)
@office_api_v1_blueprint.route('/offices/<int:office_id>', methods=['GET'])
def getoffice(office_id):
    """ This method is used to get the all political offices """
    try:
        if len(offices_data) > office_id >= 0:
            response_object = {
                'code':200,
                'party':offices_data[office_id]
            }
        else:
            response_object = {
                'code':404,
                'error':'Office not found'
            }

        return make_response(jsonify(response_object), response_object.get('status'))
    except ValueError:
        response_object = {
            'code':400,
            'data':"Please provide a valid office id"
        }
        return make_response(jsonify(response_object), 400)
