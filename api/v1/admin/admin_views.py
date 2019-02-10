""" Admin REST api Views"""

from flask import Blueprint, request, make_response, jsonify
from develop.api.v1.admin.admin_models import Parties, Offices, offices_data, parties_data

ADMIN_API_BLUEPRINT = Blueprint('admin', __name__)

@ADMIN_API_BLUEPRINT.route('/admin/parties', methods=['POST'])
def createparty():
    """ This method is used to create a party by the web site admin """
    # Get the post party data
    post_data = request.get_json(force=True)
    
    if post_data is None:
        response_object = {
            "status":400,
            "error" : 'Bad Request'
        }
    
    party = {
        'party_id':post_data['party_id'],
        'name':post_data['name'],
        'hq_address':post_data['hq_address'],
        'logo_url':post_data['logo_url']
        }

    Offices.save(party)
    response_object = {
        'status': 201,
        'data':[
            {
                'messege':'Successfully created.'
            }
        ]
    }
    return make_response(jsonify(response_object), 201)

@ADMIN_API_BLUEPRINT.route('/admin/parties', methods=['GET'])
def getallparties():
    """ This method is used to get all the political parties """
    # Get all the political offices
    response_object = {
        "status":200,
        "data":offices_data
    }
    return make_response(jsonify(response_object), 200)

@ADMIN_API_BLUEPRINT.route('/admin/parties/<int:party_id>', methods=['GET'])
def getparty(party_id):
    """ This method is used to get the specific political party """
    # Get  the political party
    party = [party for party in parties_data if party['party_id'] == party_id]
    try:
        int(party_id)
        response_object = {
            'status':200,
            'data':parties_data[party_id]
        }
        return make_response(jsonify(response_object), 200)

    except ValueError:
        response_object = {
            'status':400,
            'data':"Please provide a valid party id"
        }
        return make_response(jsonify(response_object), 400)

@ADMIN_API_BLUEPRINT.route('/admin/parties/<int:party_id>', methods=['PUT'])
def editparty(party_id):
    """ This method is used to delete the specific political party """
    post_data = request.get_json(force=True)
    try:
        int(party_id)
        if post_data is None:
            response_object = {
                "status":400,
                "error":"Bad Request"
            }
            return make_response(jsonify(response_object), 400)

        for party in parties_data:
            int(party_id)
            if party['party_id'] == party_id:
                party = {
                    'party_id':post_data.get('party_id'),
                    'name':post_data.get('name'),
                    'hq_address':post_data.get('hq_address'),
                    'logo_url':post_data.get('logo_url')
                }

            Offices.save(party)
            response_object = {
                "status":200,
                "data":{
                    "Message":"Updated Successfully"
                }
            }
        return make_response(jsonify(response_object), 200)
        
    except ValueError:
        response_object = {
            'status':400,
            'error':"Please provide a valid party id"
        }
        return make_response(jsonify(response_object), 400)
    
@ADMIN_API_BLUEPRINT.route('/admin/parties/<int:party_id>', methods=['DELETE'])
def deleteparty(party_id):
    """ This method is used to delete the specific political party """
    # Get  the political party
    party = [party for party in parties_data if party['party_id'] == party_id]
    del parties_data[party_id-1]
    response_object = {
        'status':200,
        'data':{
            'message':'Party successfully deleted'
        }
    }
    return make_response(jsonify(response_object), 200)

@ADMIN_API_BLUEPRINT.route('/admin/offices', methods=['POST'])
def createoffice():
    """ This method is used to create a political office by the web site admin """
    post_data = request.get_json(force=True)
    if post_data is None:
        response_object = {
            "status":400,
            "error":"Bad Request"
        }

    else:
        office = {
            'office_id':post_data['office_id'],
            'office_type':post_data['office_type'],
            'name':post_data['name']
        }

        Offices.save(office)

        response_object = {
            'status': 201,
            'data':[
                {
                    'messege':'Successfully created.'
                }
            ]
        }
    return make_response(jsonify(response_object), 201)

@ADMIN_API_BLUEPRINT.route('/admin/offices', methods=['GET'])
def getalloffices():
    """ This method is used to get all the political parties """
    # Get all the political offices
    response_object = {
        "status":200,
        "data":offices_data
    }
    return make_response(jsonify(response_object), 200)
@ADMIN_API_BLUEPRINT.route('/admin/offices/<int:office_id>', methods=['GET'])
def getoffice(office_id):
    """ This method is used to get the all political offices """
    office = [office for office in offices_data if office['office_id'] == office_id]

    response_object = {
        "status":200,
        "data":offices_data[office_id]
    }
    return make_response(jsonify(response_object), 200)
