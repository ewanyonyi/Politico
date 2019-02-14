""" A class for parties data Strucure """
parties_data = []

offices_data = []


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
        
