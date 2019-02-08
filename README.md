# Politico



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
1. Sign up: /api/v1/auth/signup
1. Sign in: /api/v1/auth/signin
1. Create Party: /api/v1/admin/createparty
1. Get all parties: /api/v1/admin/parties/getall
1. Get specific part: /api/v1/admin/parties/get/<id of type int>
1. Delete specific party: /api/v1/admin/parties/delete/<id of type int>
1. Edit specific party: /api/v1/admin/parties/edit/<id of type int>
1. Create a political office: /api/v1/admin/createoffice
1. Get all political offices: /api/v1/admin/offices/getall
1. Get specific political office: /api/v1/admin/offices/get/<id of type int>

### Run tests
```sh
$python run_tests.py
```