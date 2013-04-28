from django.contrib.auth.models import User

def create_superuser():
    user = User.objects.create_superuser(username='admin',
                                      password='test',
                                      email='test@test.com')
    return user

def login_admin_user(browser):
    
    browser.get("http://127.0.0.1:8081/admin")
    browser.find_element_by_name("username").send_keys("admin")
    browser.find_element_by_name("password").send_keys('test')
    browser.find_element_by_xpath('//input[@value="Log in"]').click()

def browse_to_add_activity_and_enter_name(browser,name):
    browser.get("http://127.0.0.1:8081/my_activity/add_activity")
    browser.find_element_by_name("name").send_keys(name)
    browser.find_element_by_xpath('//input[@value="Save"]').click()
    
