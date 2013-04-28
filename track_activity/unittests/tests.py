from django.utils import unittest
from django.test.client import Client


class unauthorised_user_should_not_be_able_toaccess_addactivity(unittest.TestCase):

    def test(self):
        c = Client()
        response = c.get('/my_activity/add_acivity')
        self.assertEqual(response.status_code, 404) #currently no login feature so not exists       
        
