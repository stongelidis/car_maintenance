# Car Maintenance Databasing Tool
This project is a databasing tool to help keep track of each service performed on a car. Never again wonder when was the last time you serviced your car.

## Getting Started (Running a Local Copy)

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

Use of a virtual environment is recommended  to keep dependencies independent and organized. 

#### PIP Dependencies

Install dependencies by navigating to the source directory and running:

```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, navigate to the source folder and run the following command from the terminal:
```bash
python3 manage.py db upgrade
```

## Running the server

From within the source directory execute the following to run the server: 

```bash
export DATABASE_URL=<SQLALCHEMY_DATABASE_URI>
export AUTH0_DOMAIN=dev-ukvu27nm.auth0.com
export API_AUDIENCE=car_maintenance
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## Endpoints
### GET /cars
