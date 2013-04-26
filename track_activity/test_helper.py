from django.contrib.auth.models import User

def create_superuser():
    User.objects.create_superuser(username='admin',
                                      password='test',
                                      email='test@test.com')

def login_admin_user(browser):
    
    browser.get("http://127.0.0.1:8081/admin")
    browser.find_element_by_name("username").send_keys("admin")
    browser.find_element_by_name("password").send_keys('test')
    browser.find_element_by_xpath('//input[@value="Log in"]').click()