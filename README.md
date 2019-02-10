# Politico

[![Build Status](https://travis-ci.org/emanuelwanyonyi/Politico.svg?branch=develop)](https://travis-ci.org/emanuelwanyonyi/Politico)

<a href="https://codeclimate.com/github/codeclimate/codeclimate/maintainability"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability" /></a>

<a href="https://codeclimate.com/github/codeclimate/codeclimate/test_coverage"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage" /></a>

### Basics

1. Fork/Clone https://github.com/emanuelwanyonyi/Politico.git
1. ```For windows system ```
1. Run python -m 'your cloned directory name' and move to the directory, 
change directory to Scripts and run activate file to activate the  virtualenv
1. Install the requirements in the requirements file

### Set Environment Variables

Update *server/config.py*, and then run:
### Run the Application

```sh
$ python run.py
```

Access the application at the address http://localhost:5000/``

### API End Points
---------------------------------------------------------------------------------------
|End point name                     |Method    |Endpoint url                            | 
---------------------------------------------------------------------------------------
|Sign up                            |POST      |/api/v1/auth/signup                     |
---------------------------------------------------------------------------------------
|Sign in                            |POST      |/api/v1/auth/signin                    |
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
