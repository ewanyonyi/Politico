""" A class for parties data Strucure """
parties_data = [ 
        {
            'party_id':1,
            'name':'Party 1',
            'hq_address':'Pangani, 2nd Street, Party 1 House',
            'logo_url':'/partielsdata/logs/party1'
        },
        {
            'party_id':2,
            'name':'Party 2',
            'hq_address':'West End Building, Second Floor, Waiyaki Way',
            'logo_url':'/partielsdata/logs/party3'
        },
        {
            'party_id':3,
            'name':'Party 3',
            'hq_address':'HWZ, 3rd Floor, HouseMombasa Road, Nairobi West',
            'logo_url':'/partielsdata/logs/party3'
        }
    ]

offices_data = [ 
        {
            'office_id':1,
            'office_type':'federal',
            'name':'Office 1'
        },
        {
            'office_id':2,
            'office_type':'state',
            'name':'Office 2'
        },
        {
            'office_id':1,
            'office_type':'legislative',
            'name':'Office 1'
        }
    ]


class Parties():
    """ Class for parties data """
    def __init__(self, party_id, name, hq_address, logo_url):
        self.party_id = party_id
        self.name = name
        self.hq_address = hq_address
        self.logo_url = logo_url
    def save(self):
        """ Save party method"""
        parties_data.append(self)

class Offices():
    """ Class for Offices data """
    def __init__(self, office_id, office_type, name):
        self.office_id = office_id
        self.office_type = office_type
        self.name = name

    def save(self):
        """ Save Office method """
        offices_data.append(self)
    