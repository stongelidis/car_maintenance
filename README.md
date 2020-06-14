# Car Maintenance Databasing Tool
This project is a databasing tool to help keep track of each service performed on a car. Never again wonder when was the last time you serviced your car.

## Getting Started 
### Running a Local Copy

#### Installing Dependencies

##### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

##### Virtual Environment

Use of a virtual environment is recommended  to keep dependencies independent and organized. 

##### PIP Dependencies

Install dependencies by navigating to the source directory and running:

```bash
pip install -r requirements.txt
```

###### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

#### Database Setup
With Postgres running, navigate to the source folder and run the following command from the terminal:
```bash
python3 manage.py db upgrade
```

#### Running the server

From within the source directory execute the following to run the server: 

```bash
export DATABASE_URL=<SQLALCHEMY_DATABASE_URI>
export AUTH0_DOMAIN=<INSERT Auth0 DOMAIN HERE>
export API_AUDIENCE=<INSERT Auth0 AUDIENCE HERE>
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

### Interacting with Web API 
The other option is to work with the web API. The web API is located here: https://car-maintenance-database.herokuapp.com   

## Roles
There are two roles associated with the API: admin, user, and all

### All
No user permissions are needed to get all cars or get all service endpoints

### Admin
The 'admin' role has the following RBAC associated with the user:
- get:cars
- add:cars
- patch:cars
- delete:cars
- get:services
- add:services
- patch:services
- delete:services

### User
The 'user' role has the following RBAC associated with it:
- get:cars 
- add:cars
- get:services
- add:services

## Tokens
The following token can be used to test the 'admin' roles: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImgzQ0lyeVlIMzlxY24zLXJ1TUc2USJ9.eyJpc3MiOiJodHRwczovL2Rldi11a3Z1MjdubS5hdXRoMC5jb20vIiwic3ViIjoiUDZnNERhTjVTMUtFSkZ1ZkdGQUlHc0pjVHVONzVHOTBAY2xpZW50cyIsImF1ZCI6ImNhcl9tYWludGVuYW5jZSIsImlhdCI6MTU5MjA5OTk5OSwiZXhwIjoxNTkyMTg2Mzk5LCJhenAiOiJQNmc0RGFONVMxS0VKRnVmR0ZBSUdzSmNUdU43NUc5MCIsInNjb3BlIjoiZ2V0OmNhcnMgYWRkOmNhcnMgcGF0Y2g6Y2FycyBkZWxldGU6Y2FycyBnZXQ6c2VydmljZXMgYWRkOnNlcnZpY2VzIHBhdGNoOnNlcnZpY2VzIGRlbGV0ZTpzZXJ2aWNlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpjYXJzIiwiYWRkOmNhcnMiLCJwYXRjaDpjYXJzIiwiZGVsZXRlOmNhcnMiLCJnZXQ6c2VydmljZXMiLCJhZGQ6c2VydmljZXMiLCJwYXRjaDpzZXJ2aWNlcyIsImRlbGV0ZTpzZXJ2aWNlcyJdfQ.oNl0Veb9sxP8LtM6T4deY6_tzGYzxVO2dg__S5in5Nmqyu5ePoxsmr0PJzFhq4zg5DS_gQb501R1lui30S8wQVwxWar0apbF78tmo155Xoq4YsblaLkdnQoNrtlmG4Xjfo5LLstHy5q9GQqMQNYQYbvzplEmO5NFkOsZsKtCSEqlIvn03Cc2OHV7sfoDB_616k8CN5qZuZtBloOqGkgkPfBaMc3e9btNGsfEMEpVq0m43dsFeGoUKBbH8wuqIq808BULbAIuhS-5f7fZaec57dPZD3S_AL7Z9PzdggsIj6VybNX0rpXvh1a09YSEcxfd-dF5ZdPQfgu7fOeaN0HzWA   
The following token can be used to test the 'user' roles: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImgzQ0lyeVlIMzlxY24zLXJ1TUc2USJ9.eyJpc3MiOiJodHRwczovL2Rldi11a3Z1MjdubS5hdXRoMC5jb20vIiwic3ViIjoiUDZnNERhTjVTMUtFSkZ1ZkdGQUlHc0pjVHVONzVHOTBAY2xpZW50cyIsImF1ZCI6ImNhcl9tYWludGVuYW5jZSIsImlhdCI6MTU5MjEwMDE0NiwiZXhwIjoxNTkyMTg2NTQ2LCJhenAiOiJQNmc0RGFONVMxS0VKRnVmR0ZBSUdzSmNUdU43NUc5MCIsInNjb3BlIjoiZ2V0OmNhcnMgYWRkOmNhcnMgZ2V0OnNlcnZpY2VzIGFkZDpzZXJ2aWNlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpjYXJzIiwiYWRkOmNhcnMiLCJnZXQ6c2VydmljZXMiLCJhZGQ6c2VydmljZXMiXX0.edD1FjF6uGz4fXdQl6wxXCR8-9mVT_xUi7OTCtzUqu7X0od_6k1rqy_Zq6fbmcRR60lRjIpEbVJ_NbfLERLCVgL-ZZH1_73RKrWWaid2mjQBJ5kduwNIQ4-lk5Lf_gBMqaHKiqGNx-647_SIGmdBf2Tyfbui36_Z-m_m_b6RY5Ed3X06lru-CvlwjIVjP7uKjuwW7dqCGLSZjcDkYRnWmuhThH9paLyjkrJyvs4ONYCklhIP1D1DAdz2RYvUV-9kBDh1m60_XN4_g8V9KxtxnEDnriFy3sDH1J8a3Go1u_ur_lZH3bqSC-Rj-5dEMeTNpn74Nkvie1Wk9jImc1dVsg   

## Endpoints
### GET /cars
- Gets a descriptive list of all the cars in the database
- Permissions: None
- Request Arguments: None
- Body: None
- Returns: An object with a list of car objects with the keys shown below
```
{
    "cars": [
        {
            "id": 1,
            "make": "Ford",
            "model": "Taurus",
            "year": 1994
        },
        {
            "id": 2,
            "make": "Honda",
            "model": "Accord",
            "year": 2000
        }
    ],
    "success": true
} 
```

### GET /cars/<car_id>
- Gets a specific car within the database with it's attributes
- Permissions: get:cars
- Request Arguments: car id 
- Body: None
- Returns: An object containing a car object
```
{
    "car": {
        "id": 1,
        "make": "Ford",
        "model": "Taurus",
        "year": 1994
    },
    "success": true
} 
```

### POST /cars/
- Adds a car to the database
- Permissions: post:cars
- Request Arguments: None
- Body: Parameters to define a car
```
{
	"make": "Ford",
	"model": "Bronco",
	"year": 1995
}
```
- Returns: An object containing the newly created car object
```
{
    "car": {
        "id": 4,
        "make": "Ford",
        "model": "Bronco",
        "year": 1995
    },
    "success": true
} 
```

### PATCH /cars/<car_id>
- Edits a car from the database
- Permissions: patch:cars
- Request Arguments: None
- Body: Parameters to define a car
```
{
    "make": "Honda",
    "model": "Accord",
    "year": 2000
}
```
- Returns: An object containing the newly edited car object
```
{
    "car": {
        "id": 2,
        "make": "Honda",
        "model": "Accord",
        "year": 2000
    },
    "success": true
} 
```

### DELETE /cars/<car_id>
- Deletes a car from the database
- Permissions: delete:cars
- Request Arguments: None
- Body: None
- Returns: An object containing the car id that was deleted
```
{
    "car": 2,
    "success": true
} 
```

### GET /services
- Gets a descriptive list of all services in the database
- Permissions: None
- Request Arguments: None
- Body: None
- Returns: An object with a list of service objects with the keys shown below
```
{
    "services": [
        {
            "date": "Wed, 13 May 2020 00:00:00 GMT",
            "id": 1,
            "make": "Honda",
            "mileage": 43000,
            "model": "Accord",
            "notes": "oil change, new oil filter, and new brakes"
        },
        {
            "date": "Fri, 15 May 2020 00:00:00 GMT",
            "id": 2,
            "make": "Ford",
            "mileage": 50000,
            "model": "Taurus",
            "notes": "replace steering fluid; rotate tires"
        },
        {
            "date": "Fri, 15 May 2020 00:00:00 GMT",
            "id": 3,
            "make": "Ford",
            "mileage": 50000,
            "model": "Taurus",
            "notes": "replace steering fluid; rotate tires"
        }
    ],
    "success": true
} 
```

### GET /services/<service_id>
- Get a specific service with all of it's attributes
- Permissions: get:services
- Request Arguments: services id 
- Body: None
- Returns: An object containing a service object
```
{
    "service": {
        "date": "Wed, 13 May 2020 00:00:00 GMT",
        "id": 1,
        "make": "Honda",
        "mileage": 43000,
        "model": "Accord",
        "notes": "oil change, new oil filter, and new brakes"
    },
    "success": true
} 
```

### POST /services/
- Add a new service to the database
- Permissions: post:services
- Request Arguments: None
- Body: Parameters to define a service
```
{
	"date": "2020-05-15",
	"mileage": 50000,
	"notes": "replace steering fluid; rotate tires",
	"car_id": 1
}
```
- Returns: An object containing the newly created service object
```
{
    "service": {
        "date": "Fri, 15 May 2020 00:00:00 GMT",
        "id": 3,
        "make": "Ford",
        "mileage": 50000,
        "model": "Taurus",
        "notes": "replace steering fluid; rotate tires"
    },
    "success": true
} 
```

### PATCH /services/<service_id>
- Edit a service in the database
- Permissions: patch:services
- Request Arguments: None
- Body: Parameters to define a service
```
{
	"date": "2020-05-15",
	"mileage": 50000,
	"notes": "replace steering fluid; rotate tires",
	"car_id": 1
}
```
- Returns: An object containing the newly edited car object
```
{
    "service": {
        "date": "Fri, 15 May 2020 00:00:00 GMT",
        "id": 2,
        "make": "Ford",
        "mileage": 50000,
        "model": "Taurus",
        "notes": "replace steering fluid; rotate tires"
    },
    "success": true
}
```

### DELETE /services/<service_id>
- Delete a service in the database
- Permissions: delete:services
- Request Arguments: service_id
- Body: None
- Returns: An object containing the service id that was deleted
```
{
    "service": 3,
    "success": true
} 
```

## Testing
Unit tests were created using the unittest module. The tests can be run by executing the following command within the source directory:
```bash
python3 test_app.py
```