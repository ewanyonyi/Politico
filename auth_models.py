""" A class for users data model """
import re
from datetime import datetime



class Users():
    """ Users data structure for storing users related data """
	
    users_data = [
        {
            'id':1,
            'firstname':'Emanuel',
            'lastname':'Wanyonyi',
            'othername':'Dickson',
            'email':'admin@gmail.com',
            'phoneNumber':'0703793386',
            'registered':datetime.now(),
            'passportUrl':'String',
            'isAdmin':True,
            'password':'test@1234'
        },
        {
            'id':2,
            'firstname':'Ruth',
            'lastname':'Mukunga',
            'othername':'Wamutwa',
            'email':'ruth@gmail.com',
            'phoneNumber':'0703793386',
            'registered':datetime.now(),
            'passportUrl':'String',
            'isAdmin':False,
            'password':'test1@1234'
        },
        {
            'id':3,
            'firstname':'Evans',
            'lastname':'Wanyonyi',
            'othername':'Wekesa',
            'email':'wekesa@gmail.com',
            'phoneNumber':'0703793386',
            'registered':datetime.now(),
            'passportUrl':'String',
            'isAdmin':False,
            'password':'test$1234'
        }
    ]
    
    def __init__(self, firstname=None, lastname=None, othername=None,
     phoneNumber=None, email=None, password=None):
        self.user_id = len(Users) + 1
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.phoneNumber = phoneNumber
        self.registered = datetime.now()
        self.password = password
    