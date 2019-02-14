# Politico

[![Build Status](https://travis-ci.org/emanuelwanyonyi/Politico.svg?branch=develop)](https://travis-ci.org/emanuelwanyonyi/Politico)  <a href="https://codeclimate.com/github/emanuelwanyonyi/Politico/maintainability"><img src="https://api.codeclimate.com/v1/badges/a1018e71752a814039fa/maintainability" /></a>



### Basics

1. Fork/Clone https://github.com/emanuelwanyonyi/Politico.git

## Activate Virtual Environment

1. Run python -m 'your cloned directory name' and move to the directory, 
change directory to Scripts and run activate file to activate the  virtualenv
### Install requirements
1. pip install -r requirements.txt

Update *server/config.py*, and then run:

### Run the Application
```sh
$ python manage.py runserver
```

Access the application at the address http://localhost:5000/``

### API End Points
---------------------------------------------------------------------------------------
|End point name                     |Method    |Endpoint url                            |
---------------------------------------------------------------------------------------
|Create Party                       |POST      |/api/v1/admin/parties                   |
----------------------------------------------------------------------------------------
|Get all parties                    |GET       | /api/v1/admin/parties                  |
----------------------------------------------------------------------------------------
|Get specific part                  |GET       |/api/v1/admin/parties/party_id          |
---------------------------------------------------------------------------------------
|Delete specific party              |DELETE    | /api/v1/admin/parties/party_id        |
---------------------------------------------------------------------------------------
|Edit specific party                | PUT      | /api/v1/admin/parties/party_id         |
----------------------------------------------------------------------------------------
|Create a political office          | POST     |/api/v1/admin/offices                   |
----------------------------------------------------------------------------------------
|Get all political offices          |GET       | /api/v1/admin/offices                  |
----------------------------------------------------------------------------------------
|Get specific political office      | GET      | /api/v1/admin/offices/office_id        |
-----------------------------------------------------------------------------------------
