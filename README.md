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
The following token can be used to test the 'admin' roles:   
The following token can be used to test the 'user' roles:   

## Endpoints
### GET /cars
- Fetches a list containing all cars within the database
- Permissions: None
- Request Arguments: None
- Returns: An object with a 
```'
adfadf 
```

### GET /cars/<car_id>
- <INSERT DESCRIPTION
- Permissions: get:cars
- Request Arguments: car id 
- Returns: 
```'
adfadf 
```

### POST /cars/
- INSERT DESCRIPTION
- Permissions: post:cars
- Request Arguments: None
- Returns: 
```'
adfadf 
```

### PATCH /cars/<car_id>
- INSERT DESCRIPTION
- Permissions: patch:cars
- Request Arguments: None
- Returns: 
```'
adfadf 
```

### DELETE /cars/<car_id>
- INSERT DESCRIPTION
- Permissions: delete:cars
- Request Arguments: None
- Returns: 
```'
adfadf 
```

### GET /services
- Fetches a list containing all services within the database
- Permissions: None
- Request Arguments: None
- Returns: 
```'
adfadf 
```

### GET /services/<service_id>
- <INSERT DESCRIPTION
- Permissions: get:services
- Request Arguments: services id 
- Returns: 
```'
adfadf 
```

### POST /services/
- INSERT DESCRIPTION
- Permissions: post:services
- Request Arguments: None
- Returns: 
```'
adfadf 
```

### PATCH /services/<service_id>
- INSERT DESCRIPTION
- Permissions: patch:services
- Request Arguments: None
- Returns: 
```'
adfadf 
```

### DELETE /services/<service_id>
- INSERT DESCRIPTION
- Permissions: delete:services
- Request Arguments: None
- Returns: 
```'
adfadf 
```

## Testing
Unit tests were created using the unittest module. The tests can be run by executing the following command within the source directory:
```bash
python3 test_app.py
```