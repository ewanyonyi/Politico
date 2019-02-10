""" Data validation moule """
import re

class Validator():
    """ Validation class """
    def __init__(self, email, password):
        self.email = email
        self.password = password

    

    def validate_email(email):
        """Validates the email """
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            result = 'Invalid email!'
        else:
            result = 1

        return result

    def validate_password(password):
        """ Validates the Password """
        if len(password) < 6:
            result = 'The password field should be more than 6 characters'

        elif not re.search("[a-z]", password):
            result = 'The password field should have at least 1 lowercase letter!'

        elif not re.search("[A-Z]", password):
            result = 'The password field should have at least 1 uppercase letter!'

        elif not re.search("[0-9]", password):
            result = 'The password field should have at least 1 number!'

        elif not re.search("[_@$#!*]", password):
            result = 'The password field should have at least _ @ $ # ! *'

        else:
            result = 1 
        return result

