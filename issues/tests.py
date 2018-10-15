
# Create your tests here.
import unittest
from django.test import Client


class TestStaffCase(unittest.TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.client.login(username='staff_user', password='staurofilakes87')

    def test_list(self):
        # Issue a GET request.
        response = self.client.get('/issues/issue/')

        # Check that the response is 200 OK.
        # self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertGreaterEqual(len(response.context['issues']), 1)

    def test_creation(self):
        response = self.client.post('/issues/issue/add', {
            'submitter': '1', 'description': 'test issue'
        })
        self.assertEqual(response.status_code, 403)


class SuperuserTest(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.client.login(username='app_superuser', password='iddqdidkfa87')

    def test_list(self):
        # Issue a GET request.
        response = self.client.get('/issues/issue/')

        # Check that the response is 200 OK.
        # self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertGreaterEqual(len(response.context['issues']), 1)

    def test_creation(self):
        response = self.client.post('/issues/issue/add/', {
            'submitter': '1', 'description': 'test issue'
        })

        # self.assertEqual(response.status_code, 200)

        response = self.client.get('/admin/issues/')
        # self.assertEqual(response.status_code, 200)

        self.assertGreaterEqual(len(response.context['issues']), 2)
