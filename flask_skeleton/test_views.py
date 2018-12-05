import pytest
import os
from flask_skeleton import app, views
import unittest
import json

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_health(self):
        r = self.app.get('/health')
        data = r.get_json()

        self.assertEqual(data['result'] , "Hello.")
