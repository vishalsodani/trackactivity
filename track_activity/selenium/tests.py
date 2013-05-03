from django.test import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from test_helper import create_superuser,login_admin_user,browse_to_add_activity_and_enter_name



class authorised_user_should_be_able_to_add_an_activity(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        
    def test(self):
        """
        Create an admin user, login, browse to add_activity,add an activity and confirm activity added.
        """
        create_superuser()

        
        login_admin_user(self.browser)
        browse_to_add_activity_and_enter_name(self.browser,'Walking')
        elem = self.browser.find_element_by_xpath('//td[1]')
        
        self.assertEqual(elem.text, 'Walking')



class authorised_user_should_not_be_able_to_add_an_empty_activity(LiveServerTestCase):
    def test(self):
        """
        Create an admin user, login, browse to add_activity,add an empty activity and confirm error message.
        """
        create_superuser()

        browser = webdriver.Firefox()
        login_admin_user(browser)
        browse_to_add_activity_and_enter_name(browser,"")
        elem = browser.find_element_by_xpath('//ul[@class="errorlist"]')
        
        self.assertEqual(elem.text, 'This field is required.')
        browser.quit()
    
        
