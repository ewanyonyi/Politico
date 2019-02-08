# Politico



### Basics

1. Fork/Clone https://github.com/emanuelwanyonyi/Politico.git
```For windows system ```
1. Run python -m 'your cloned directory name' and move to the directory, 
change directory to Scripts and run activate file to activate the  virtualenv
1. Install the requirements in the requirements file

### Set Environment Variables

Update *config.py*, and then run:
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
|Sign in                            |POST      |/api/v1/admin/createparty               |
---------------------------------------------------------------------------------------
|Create Party                       |POST      |/api/v1/admin/createparty               |
----------------------------------------------------------------------------------------
|Get all parties                    |GET       | /api/v1/admin/parties/getal             |
----------------------------------------------------------------------------------------
|Get specific part                  |GET       |/api/v1/admin/parties/get/party_id       |
---------------------------------------------------------------------------------------
|Delete specific party              |DELETE    | /api/v1/admin/parties/delete/party_id   |
---------------------------------------------------------------------------------------
|Edit specific party                | PUT      | /api/v1/admin/parties/edit/party_id     |
----------------------------------------------------------------------------------------
|Create a political office          | POST     |/api/v1/admin/createoffice                |
----------------------------------------------------------------------------------------
|Get all political offices          |GET       | /api/v1/admin/offices/getall            |
----------------------------------------------------------------------------------------
|Get specific political office      | GET      | /api/v1/admin/offices/get/office_id      |
-----------------------------------------------------------------------------------------



### Run tests
```sh
$python run_tests.py
```
