"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
import time
from django.test import LiveServerTestCase


class authorised_user_should_be_able_to_add_an_activity(LiveServerTestCase):
    def test(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        User.objects.create_superuser(username='admin',
                                      password='test',
                                      email='test@test.com')

        browser = webdriver.Firefox()
        browser.get("http://127.0.0.1:8081/admin")
        browser.find_element_by_name("username").send_keys("admin")
        browser.find_element_by_name("password").send_keys('test')
        browser.find_element_by_xpath('//input[@value="Log in"]').click()
        browser.get("http://127.0.0.1:8081/my_activity/add_activity")
        browser.find_element_by_name("name").send_keys("Walking")
        browser.find_element_by_xpath('//input[@value="Save"]').click()
        elem = browser.find_element_by_xpath('//td[1]')
        self.assertEqual(elem.text, 'Walking')
        browser.quit()

        
        
