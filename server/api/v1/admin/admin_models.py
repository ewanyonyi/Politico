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
    def __init__(self):
        self.parties_data = parties_data

    def save(self):
        """ Save party method"""
        parties_data.append(self)

    

class Offices():
    """ Class for Offices data """
    def __init__(self):
        
        self.offices_data = offices_data


    def save(self):
        """ Save Office method """
        offices_data.append(self)
        
