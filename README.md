# Politico

[![Build Status](https://travis-ci.org/realpython/flask-jwt-auth.svg?branch=develop)](https://travis-ci.org/realpython/flask-jwt-auth)

### Basics

1. Fork/Clone
1. Activate a virtualenv
1. Install the requirements

### Set Environment Variables

Update *config.py*, and then run:
### Run the Application

```sh
$ python run.py
```


Access the application at the address http://localhost:5000/``

### API End Points
a. Sign up: /api/v1/auth/signup
b. Sign in: /api/v1/auth/signin
c. Create Party: /api/v1/admin/createparty
d. Get all parties: /api/v1/admin/parties/getall
e. Get specific part: /api/v1/admin/parties/get/<id of type int>
f. Delete specific party: /api/v1/admin/parties/delete/<id of type int>
g. Edit specific party: /api/v1/admin/parties/edit/2
h. Create a political office: /api/v1/admin/createoffice
i. Get all political offices: /api/v1/admin/offices/getall
j. Get specific political office: /api/v1/admin/offices/get/1

### Run tests
```sh
$python run_tests.py
```
