""" Admin REST api Views"""

from flask import Blueprint, request, make_response, jsonify
from server.api.v1.admin.admin_models import Parties, Offices, offices_data, parties_data

admin_api_v1_blueprint = Blueprint('admin', __name__)

@admin_api_v1_blueprint.route('/parties', methods=['POST'])
def createparty():
    """ This method is used to create a party by the web site admin """
    # Get the post party data
    post_data = request.get_json(force=True)
    if post_data is None:
        response_object = {
            "code":400,
            "error" : 'Bad Request'
        }
    else:
        party = {
            'name':post_data['name'],
            'hq_address':post_data['hq_address'],
            'logo_url':post_data['logo_url']
        }

    
        stored_party_names = [d.get('name') for d in parties_data]
        if post_data['name'] in stored_party_names:
            response_object = {
                "code":409,
                "error":"Party name already exist !"
            }
        else:
            Parties.save(party)
            response_object = {
                'code': 201,
                'party':[
                    { 
                        'id':parties_data.index(party),
                        'name':post_data['name'],
                        'hq_address':post_data['hq_address'],
                        'logo_url':post_data['logo_url']
                    }
                ]
            }
    return make_response(jsonify(response_object), response_object.get('status'))

@admin_api_v1_blueprint.route('/parties', methods=['GET'])
def getallparties():
    """ This method is used to get all the political parties """
    # Get all the political offices
    response_object = {
        "code":200,
        "Parties":parties_data
    }
    return make_response(jsonify(response_object), response_object.get('status'))

@admin_api_v1_blueprint.route('/parties/<int:party_id>', methods=['GET'])
def getparty(party_id):
    """ This method is used to get the specific political party """
    try:       
        if len(parties_data) > party_id >= 0:
            response_object = {
                'code':200,
                'party':parties_data[party_id]
            }
        else:
            response_object = {
                'code':404,
                'error':'Party not found'
            }

        return make_response(jsonify(response_object), response_object.get('status'))

    except ValueError:
        response_object = {
            'code':400,
            'data':"Please provide a valid party id"
        }
        return make_response(jsonify(response_object), response_object.get('status'))

@admin_api_v1_blueprint.route('/parties/<int:party_id>', methods=['PUT'])
def editparty(party_id):
    """ This method is used to delete the specific political party """
    post_data = request.get_json(force=True)
    try:
        if post_data is None:
            response_object = {
                "code":400,
                "error":"Bad Request, please check your inputs"
            }

        elif party_id > len(parties_data) or party_id < 0:
            response_object = {
                'code':404,
                'error':"Party not found"
            }
        else:
            new_party = {
                'name':post_data.get('name'),
                'hq_address':post_data.get('hq_address'),
                'logo_url':post_data.get('logo_url')
            }

            parties_data[party_id] = new_party
            response_object = {
                "code":200,
                "updated party":{
                    'id':parties_data.index(new_party),
                    'name':post_data.get('name'),
                    'hq_address':post_data.get('hq_address'),
                    'logo_url':post_data.get('logo_url')
                }
            }
            
                
        return make_response(jsonify(response_object), response_object.get('status'))
        
    except ValueError:
        response_object = {
            'code':400,
            'error':"Please provide a valid party id"
        }
        return make_response(jsonify(response_object), 400)
    
@admin_api_v1_blueprint.route('/parties/<int:party_id>', methods=['DELETE'])
def deleteparty(party_id):
    """ This method is used to delete the specific political party """
    try:       
        if len(parties_data) > party_id >= 0:
            del parties_data[party_id]
            response_object = {
                'code':200,
                'data':{
                    'message':'Party successfully deleted'
                }
            }
        else:
            response_object = {
                'code':404,
                'error':'Party not found'
            }

        return make_response(jsonify(response_object), response_object.get('status'))

    except ValueError:
        response_object = {
            'code':400,
            'data':"Please provide a valid party id"
        }
        return make_response(jsonify(response_object), response_object.get('status'))

@admin_api_v1_blueprint.route('/offices', methods=['POST'])
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

@admin_api_v1_blueprint.route('/offices', methods=['GET'])
def getalloffices():
    """ This method is used to get all the political parties """
    # Get all the political offices
    response_object = {
        "code":200,
        "data":offices_data
    }
    return make_response(jsonify(response_object), 200)
@admin_api_v1_blueprint.route('/offices/<int:office_id>', methods=['GET'])
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
