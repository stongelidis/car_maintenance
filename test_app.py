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

    def tearDown(self):
        """Executed after reach test"""
        pass

    # test get all cars endpoints
    def test_get_cars(self):
        res = self.client().get('/cars')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['cars'])

    # test get all services endpoint
    def test_get_services(self):
        res = self.client().get('/services')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['services'])
