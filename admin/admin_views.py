""" Admin REST api Views"""

from flask import Blueprint, request, make_response, jsonify
from develop.api.v1.admin.admin_models import Parties, Offices, offices_data, parties_data

ADMIN_API_BLUEPRINT = Blueprint('admin', __name__)

@ADMIN_API_BLUEPRINT.route('/admin/createparty', methods=['POST'])
def createparty():
    """ This method is used to create a party by the web site admin """
    # Get the post party data
    post_data = request.get_json(force=True)
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
    else:
        party = Parties(
            party_id=post_data.get('party_id'),
            name=post_data.get('name'),
            hq_address=post_data.get('hq_address'),
            logo_url=post_data.get('logo_url')
        )
        party.save()
        response_object = {
            'status': 201,
            'data':[
                {
                    'messege':'Successfully created.'
                }
            ]
        }
    return make_response(jsonify(response_object))

@ADMIN_API_BLUEPRINT.route('/admin/parties/getall', methods=['GET'])
def getallparties():
    """ This method is used to get all the political parties """
    # Get all the political offices
    response_object = {
        "status":200,
        "data":parties_data
    }
    return make_response(jsonify(response_object))

@ADMIN_API_BLUEPRINT.route('/admin/parties/get/<int:party_id>', methods=['GET'])
def getparty(party_id):
    """ This method is used to get the specific political party """
    # Get  the political party
    party = [party for party in parties_data if party['party_id'] == party_id]
    response_object = {
        'status':200,
        'data':party[0]
    }
    return make_response(jsonify(response_object))

@ADMIN_API_BLUEPRINT.route('/admin/parties/edit/<int:party_id>', methods=['PUT'])
def editparty(party_id):
    """ This method is used to delete the specific political party """
    post_data = request.get_json(force=True)
    for party in parties_data:
        if party['party_id'] == party_id:
            post_data = request.get_json()
            party['party_id'] = post_data['party_id']
            party['name'] = post_data['name']
            party['hq_address'] = post_data['hq_address']
            party['logo_url'] = post_data['logo_url']

            response_object = {
                'status': 200,
                'data':[
                    {
                        'massege':"ok",
                        'party':party
                    }
                ]
            }
            return make_response(jsonify(response_object))
        if post_data is None:
            response_object = {
                "status":400,
                "error":"Bad Request"
            }
        else:
            updated_party = Parties(
                party_id=post_data.get('party_id'),
                name=post_data.get('name'),
                hq_address=post_data.get('hq_address'),
                logo_url=post_data.get('logo_url')
            )
            updated_party.save()

            response_object = {
                'status': 201,
                'data':[
                    {
                        'party_id':post_data['party_id'],
                        'name':post_data['name'],
                        'hq_address':post_data['hq_ddress'],
                        'logo_url':post_data['logo_url']
                    }
                ]
            }
        return make_response(jsonify(response_object))  
@ADMIN_API_BLUEPRINT.route('/admin/parties/delete/<int:party_id>', methods=['DELETE'])
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
    return make_response(jsonify(response_object))

@ADMIN_API_BLUEPRINT.route('/admin/createoffice', methods=['POST'])
def createoffice():
    """ This method is used to create a political office by the web site admin """
    # Get the post political office data
    post_data = request.get_json(force=True)
    if post_data is None:
        response_object = {
            "status":400,
            "error":"Bad Request"
        }

    else:
        post_data = request.get_json()
        office = Offices(
            office_id=post_data.get('office_id'),
            office_type=post_data.get('office_type'),
            name=post_data.get('name')
        )

        office.save()

        response_object = {
            'status': 201,
            'data':[
                {
                    'office_id':post_data['office_id'],
                    'office_type':post_data['office_type'],
                    'name':post_data['name']
                }
            ]
        }
    return make_response(jsonify(response_object))
@ADMIN_API_BLUEPRINT.route('/admin/offices/getall', methods=['GET'])
def getalloffices():
    """ This method is used to get all the political parties """
    # Get all the political offices
    response_object = {
        "status":200,
        "data":offices_data
    }
    return make_response(jsonify(response_object))
@ADMIN_API_BLUEPRINT.route('/admin/offices/get/<int:office_id>', methods=['GET'])
def getoffice(office_id):
    """ This method is used to get the all political offices """
    office = [office for office in offices_data if office['office_id'] == office_id]

    response_object = {
        "status":200,
        "data":office[0]
    }
    return make_response(jsonify(response_object))
