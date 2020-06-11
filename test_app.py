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

        admin_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImgzQ0lyeVlIMzlxY24zLXJ1TUc2USJ9.eyJpc3MiOiJodHRwczovL2Rldi11a3Z1MjdubS5hdXRoMC5jb20vIiwic3ViIjoiUDZnNERhTjVTMUtFSkZ1ZkdGQUlHc0pjVHVONzVHOTBAY2xpZW50cyIsImF1ZCI6ImNhcl9tYWludGVuYW5jZSIsImlhdCI6MTU5MTgzNTQyNCwiZXhwIjoxNTkxOTIxODI0LCJhenAiOiJQNmc0RGFONVMxS0VKRnVmR0ZBSUdzSmNUdU43NUc5MCIsInNjb3BlIjoiZ2V0OmNhcnMgYWRkOmNhcnMgcGF0Y2g6Y2FycyBkZWxldGU6Y2FycyBnZXQ6c2VydmljZXMgYWRkOnNlcnZpY2VzIHBhdGNoOnNlcnZpY2VzIGRlbGV0ZTpzZXJ2aWNlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpjYXJzIiwiYWRkOmNhcnMiLCJwYXRjaDpjYXJzIiwiZGVsZXRlOmNhcnMiLCJnZXQ6c2VydmljZXMiLCJhZGQ6c2VydmljZXMiLCJwYXRjaDpzZXJ2aWNlcyIsImRlbGV0ZTpzZXJ2aWNlcyJdfQ.j8z8smhDLA_5_7t509yKe-MLzSDZDnKlOIr5gUIrp6gaPdUDMpYcqWsdCMLivAbIW2dnvepmGcGTyKlwr8gA3h4WU8V1traxxFHlqXhVc2vpkXb214LbcFI8faYdngFNmrvKyNe2bxhnBLiftMKCjxwZEUGpah8HCkijp17FqItdIIJsAj5KzsTTBTLaPCoMWp4BvgR83b1IyWGbFaMUsKI-_KkFFdGVsP72GMiWjRka5GSnpQoNKU-6RnCjjmT0jQpqNntyIlr5FBLkpk_ZfHtVihfgDXzF2vKgjQb1GeBE5lGOmJPvmuMaI8qPXTj3TVfO7g1PRIgiSYIF-vunQA'
        user_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImgzQ0lyeVlIMzlxY24zLXJ1TUc2USJ9.eyJpc3MiOiJodHRwczovL2Rldi11a3Z1MjdubS5hdXRoMC5jb20vIiwic3ViIjoiUDZnNERhTjVTMUtFSkZ1ZkdGQUlHc0pjVHVONzVHOTBAY2xpZW50cyIsImF1ZCI6ImNhcl9tYWludGVuYW5jZSIsImlhdCI6MTU5MTgzODMwMiwiZXhwIjoxNTkxOTI0NzAyLCJhenAiOiJQNmc0RGFONVMxS0VKRnVmR0ZBSUdzSmNUdU43NUc5MCIsInNjb3BlIjoiZ2V0OmNhcnMgYWRkOmNhcnMgZ2V0OnNlcnZpY2VzIGFkZDpzZXJ2aWNlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpjYXJzIiwiYWRkOmNhcnMiLCJnZXQ6c2VydmljZXMiLCJhZGQ6c2VydmljZXMiXX0.BhnMSD2wEHvEVFsQxH2A8kG3ma-Rs-oByuxPFAUejOdXJDz8IkQJFfyr2-uOWKss-Ilh_fJTpHyZHk6fcJOIg01LZG3LYSzRcDGbhgqkPwELVN0LVsyaBZTcmL05sm1HWbnaoL5Az0Y_OSpffx4AP5rNbMLRV9iAvCMxzRUdb3Wf9LH8KY_uSj7b4GoUzNjj16BtQkFEejuANBpiDvSxs0gM4T0cSo_riCE-XuOquewnUI80uUwMfwBofpHl_vjhK3Zk7QSdYO-KK5wzEcs8ijPHwb7DKevtHKI3lDaGt-bcV-OFstv794ZcFPAr_GlejOV9eMdwpHMs2TwW34e4lw'
        self.headers = {"Authorization": "Bearer {}".format(admin_token)}

        self.new_car = {
            "make": "Ford",
            "model": "Bronco",
            "year": 1995
        }

        self.new_service = {
            "date": "2020-05-15",
            "mileage": 50000,
            "notes": "replace steering fluid; rotate tires",
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
        res = self.client().get('/cars/2', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('car' in data)

    # test specific car, failure
    def test_specific_car_failure(self):
        res = self.client().get('/cars/1000', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # -------------------------------------------------------------------------
    # post in cars database
    def test_post_car(self):
        res = self.client().post('/cars', headers=self.headers, json=self.new_car)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('car' in data)

        # reset database
        id_car = data['car']['id']
        self.client().delete('/cars/%i' % id_car, headers=self.headers)

    # test post car, failure
    def test_post_car_failure(self):
        res = self.client().post('/cars', headers=self.headers, json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    # -------------------------------------------------------------------------
    # delete entry in cars database
    def test_delete_car(self):

        # add car to be deleted
        res = self.client().post('/cars', headers=self.headers, json=self.new_car)
        data = json.loads(res.data)
        car_id = data['car']['id']

        # test delete endpoint
        res = self.client().delete('/cars/%i' % car_id, headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('car' in data)

    # test delete car, failure
    def test_delete_car_failure(self):
        res = self.client().delete('/cars/1001', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # -------------------------------------------------------------------------
    # patch cars database
    def test_patch_car(self):

        # add car to be patched
        res = self.client().post('/cars', headers=self.headers, json=self.new_car)
        data = json.loads(res.data)
        car_id = data['car']['id']

        # edit entry
        data['car']['model'] = 'Fiesta'

        # patch entry
        res = self.client().patch('/cars/%i' % car_id, headers=self.headers, json=data['car'])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('car' in data)

        # reset database
        id_car = data['car']['id']
        self.client().delete('/cars/%i' % id_car, headers=self.headers)

    # test patch car, failure
    def test_patch_car_failure(self):
        res = self.client().patch('/cars/1', headers=self.headers, json={})
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

# -------------------------------------------------------------------------
    # get a specific service from database
    def test_specific_service(self):
        res = self.client().get('/services/1', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('service' in data)

    # test specific service, failure
    def test_specific_service_failure(self):
        res = self.client().get('/services/1000', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # -------------------------------------------------------------------------
    # post in services database
    def test_service_car(self):
        res = self.client().post('/services', headers=self.headers, json=self.new_service)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('service' in data)

        # reset database
        id_car = data['service']['id']
        self.client().delete('/services/%i' % id_car, headers=self.headers)

    # test post services, failure
    def test_post_service_failure(self):
        res = self.client().post('/services', headers=self.headers, json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    # -------------------------------------------------------------------------
    # delete entry in cars database
    def test_delete_services(self):

        # add service to be deleted
        res = self.client().post('/services', headers=self.headers, json=self.new_service)
        data = json.loads(res.data)
        service_id = data['service']['id']

        # test delete endpoint
        res = self.client().delete('/services/%i' % service_id, headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('service' in data)

    # test delete car, failure
    def test_delete_service_failure(self):
        res = self.client().delete('/services/1001', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # -------------------------------------------------------------------------
    # patch services database
    def test_patch_services(self):

        # add service to be patched
        res = self.client().post('/services', headers=self.headers, json=self.new_service)
        data = json.loads(res.data)
        service_id = data['service']['id']

        # edit entry
        data['service']['notes'] = 'replace brake fluid'

        # patch entry
        res = self.client().patch('/services/%i' % service_id, headers=self.headers, json=data['service'])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('service' in data)

        # reset database
        id_service = data['service']['id']
        self.client().delete('/services/%i' % id_service, headers=self.headers)

    # test patch services, failure
    def test_patch_services_failure(self):
        res = self.client().patch('/services/1', headers=self.headers, json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
