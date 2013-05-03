from django.test import TestCase
from selenium import webdriver
import time
from test_helper import create_superuser,login_admin_user,browse_to_add_activity_and_enter_name
from base_selenium import BaseSelenium



class authorised_user_should_be_able_to_add_an_activity(BaseSelenium):

    
        
    def test(self):
        """
        Create an admin user, login, browse to add_activity,add an activity and confirm activity added.
        """
        create_superuser()

        
        login_admin_user(self.browser)
        browse_to_add_activity_and_enter_name(self.browser,'Walking')
        elem = self.browser.find_element_by_xpath('//td[1]')
        
        self.assertEqual(elem.text, 'Walking')



class authorised_user_should_not_be_able_to_add_an_empty_activity(BaseSelenium):
    def test(self):
        """
        Create an admin user, login, browse to add_activity,add an empty activity and confirm error message.
        """
        create_superuser()


        login_admin_user(self.browser)
        browse_to_add_activity_and_enter_name(self.browser,"")
        elem = self.browser.find_element_by_xpath('//ul[@class="errorlist"]')
        
        self.assertEqual(elem.text, 'This field is required.')

    
        
