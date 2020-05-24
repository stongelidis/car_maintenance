import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from database.model import setup_db, Car, Service


class CarMaintenanceTesting(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.new_car = {
            "make": "Ford",
            "model": "Bronco",
            "year": 1995
        }

        self.modify_car = {
            "make": "Ford",
            "model": "Explorer",
            "year": 1997
        }

        self.new_service = {
            "date": "2020-05-15",
            "mileage": 50000,
            "service_notes": "replace steering fluid; rotate tires",
            "car_id": 1
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # -------------------------------------------------------------------------
    # test get all cars endpoints
    def test_get_cars(self):
        res = self.client().get('/cars')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('cars' in data)

    # -------------------------------------------------------------------------
    # get a specific car from database
    def test_specific_car(self):
        res = self.client().get('/cars/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('car' in data)

    # test specific car, failure
    def test_specific_car_failure(self):
        res = self.client().get('/cars/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # -------------------------------------------------------------------------
    # post in cars database
    def test_post_car(self):
        res = self.client().post('/cars', json=self.new_car)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('car' in data)

        # reset database
        id_car = data['car']['id']
        self.client().delete('/cars/%i' % id_car)

    # test post car, failure
    def test_post_car_failure(self):
        res = self.client().post('/cars', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    # -------------------------------------------------------------------------
    # delete entry in cars database
    def test_delete_car(self):

        # add car to be deleted
        res = self.client().post('/cars', json=self.new_car)
        data = json.loads(res.data)
        car_id = data['car']['id']

        # test delete endpoint
        res = self.client().delete('/cars/%i' % car_id)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('car' in data)

    # test delete car, failure
    def test_delete_car_failure(self):
        res = self.client().delete('/cars/1001')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # -------------------------------------------------------------------------
    # patch cars database
    def test_patch_car(self):

        # add car to be patched
        res = self.client().post('/cars', json=self.new_car)
        data = json.loads(res.data)
        car_id = data['car']['id']

        # edit entry
        data['car']['model'] = 'Fiesta'

        # patch entry
        res = self.client().patch('/cars/%i' % car_id, json=data['car'])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('car' in data)

        # reset database
        id_car = data['car']['id']
        self.client().delete('/cars/%i' % id_car)

    # test patch car, failure
    def test_patch_car_failure(self):
        res = self.client().patch('/cars/1', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # test get all services endpoint
    def test_get_services(self):
        res = self.client().get('/services')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['services'])
