from django.test import LiveServerTestCase
from selenium import webdriver

class BaseSelenium(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
