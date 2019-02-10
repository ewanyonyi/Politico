""" A class for users data model """

users_data = [
        {
            'id':1,
            'firstname':'Emanuel',
            'lastname':'Wanyonyi',
            'othername':'Dickson',
            'email':'admin@gmail.com',
            'phone_number':'0703793386', 
            'passport_url':'String',
            'is_admin':True,
            'password':'test@1234'
        },
        {
            'id':2,
            'firstname':'Ruth',
            'lastname':'Mukunga',
            'othername':'Wamutwa',
            'email':'ruth@gmail.com',
            'phone_number':'0703793386',
            'passport_url':'String',
            'is_admin':False,
            'password':'test1@1234'
        },
        {
            'id':3,
            'firstname':'Evans',
            'lastname':'Wanyonyi',
            'othername':'Wekesa',
            'email':'wekesa@gmail.com',
            'phone_number':'0703793386',
            'passport_url':'String',
            'is_admin':False,
            'password':'test$1234'
        }
    ]


class Users():
    """ Users data structure for storing users related data """
    def __init__(self, id, firstname, lastname, othername, email, phone_number,
                 passport_url, is_admin, password):
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phone_number = phone_number
        self.passport_url = passport_url
        self.is_admin = is_admin
        self.password = password
    
    def save(self):
        users_data.append(self)
