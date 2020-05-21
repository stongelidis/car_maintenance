import os
import json

from flask import Flask, request, jsonify, abort
from database.model import setup_db, Car, Service, db
from auth.auth import AuthError, requires_auth


app = Flask(__name__)
setup_db(app)

# -----------------------------------------------------------------------------
# get all cars or services
# -----------------------------------------------------------------------------


@app.route('/cars', methods=['GET'])
def get_cars():

    try:
        selection = Car.query.all()
        cars = list(map(Car.format, selection))

        return jsonify({
            'success': True,
            'cars': cars
        })

    except BaseException:
        abort(404)


@app.route('/services', methods=['GET'])
def get_services():

    try:
        selection = Service.query.all()
        services = list(map(Service.format, selection))

        return jsonify({
            'success': True,
            'services': services
        })

    except BaseException:
        abort(404)


# -----------------------------------------------------------------------------
# get specific cars or service
# -----------------------------------------------------------------------------


@app.route('/cars/<int:id>', methods=['GET'])
def get_specific_car(id):

    try:
        selection = Car.query.filter(Car.id == id).one_or_none()
        selected_car = selection.format()

        return jsonify({
            'success': True,
            'car': selected_car
        })

    except BaseException:
        abort(404)


@app.route('/services/<int:id>', methods=['GET'])
def get_specific_service(id):

    try:
        selection = Service.query.filter(Service.id == id).one_or_none()
        selected_service = selection.format()

        return jsonify({
            'success': True,
            'service': selected_service
        })

    except BaseException:
        abort(404)


# -----------------------------------------------------------------------------
# delete specific cars or service
# -----------------------------------------------------------------------------


@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):

    try:
        car = Car.query.get(id)
        car.delete()

        return jsonify({
            'success': True,
            'car': id
        })

    except BaseException:
        abort(404)


@app.route('/services/<int:id>', methods=['DELETE'])
def delete_service(id):

    try:
        service = Service.query.get(id)
        service.delete()

        return jsonify({
            'success': True,
            'service': id
        })

    except BaseException:
        abort(404)


# -----------------------------------------------------------------------------
# post a new car or service
# -----------------------------------------------------------------------------


@app.route('/cars', methods=['POST'])
def post_car():

    body = request.get_json()

    try:

        car_make = body.get('make')
        car_model = body.get('model')
        car_year = body.get('year')

        new_car = Car(make=car_make, model=car_model, year=car_year)
        new_car.insert()

        car_description = new_car.format()

        return jsonify({
            'success': True,
            'car': car_description
        })

    except BaseException:

        abort(422)


@app.route('/services', methods=['POST'])
def post_services():

    body = request.get_json()

    try:

        service_date = body.get('date')
        service_mileage = body.get('mileage')
        service_notes = body.get('service_notes')
        car_id = body.get('car_id')

        new_service = Service(date=service_date, mileage=service_mileage,
                              notes=service_notes, car_id=car_id)
        new_service.insert()

        service_description = new_service.format()

        return jsonify({
            'success': True,
            'service': service_description
        })

    except BaseException:

        abort(422)


# -----------------------------------------------------------------------------


@app.route('/')
def hello_world():
    return 'Hello World!'

# -----------------------------------------------------------------------------
# Error Handlers
# -----------------------------------------------------------------------------


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(403)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "user not permitted"
    }), 403


@app.errorhandler(AuthError)
def authentication_failed(auth_error):
    return jsonify({
        "success": False,
        "error": auth_error.status_code,
        "message": auth_error.error}), auth_error.status_code


if __name__ == '__main__':
    app.run()
