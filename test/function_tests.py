from selenium import webdriver
from time import sleep
import unittest
# base_url
base_url = 'http://127.0.0.1:8000/'


# 测试主界面
class IndexTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.register_url = base_url+'register/'
        self.login_url = base_url+'login/'
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        sleep(2)

    def tearDown(self):
        self.driver.close()

    # 测试进入注册界面
    def test_register(self):
        self.driver.find_element_by_id('register').click()
        sleep(2)
        self.assertEqual(self.driver.current_url, self.register_url)

    # 测试进入注册界面
    def test_login(self):
        self.driver.find_element_by_id('login').click()
        sleep(2)
        self.assertEqual(self.driver.current_url, self.login_url)


# 测试注册功能register
class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.register_url = self.base_url+'register/'
        self.driver.get(self.register_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    # 测试注册成功
    def test_register(self):
        self.driver.find_element_by_name('user_name').send_keys('zyl')
        self.driver.find_element_by_name('user_email').send_keys('zhulilong@163.com')
        self.driver.find_element_by_name('user_phone').send_keys('12332112332')
        self.driver.find_element_by_name('user_password').send_keys('zyl123')
        self.driver.find_element_by_id('register').click()
        sleep(2)


# 测试登录功能login
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.login_url = self.base_url+'login/'
        self.driver.get(self.login_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    # 测试登录成功
    def test_login(self):
        self.driver.find_element_by_name('user_email').send_keys('lilinyu861@outlook.com')
        self.driver.find_element_by_name('user_password').send_keys('abc123')
        self.driver.find_element_by_id('login').click()
        sleep(2)


# 测试接口测试
class TestInterface(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.interface_url = self.base_url+'tools/interfacetest/'
        self.driver.get(self.interface_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_json_data(self):
        self.driver.find_element_by_name('method').send_keys('GET')
        self.driver.find_element_by_name('request-url').send_keys('https://www.baidu.com/')
        self.driver.find_element_by_name('request-header').send_keys('')
        self.driver.find_element_by_name('request-body').send_keys('')
        self.driver.find_element_by_name('send_submit').click()
        print(self.driver.page_source)
        sleep(2)


if __name__ == '__main__':
    unittest.main()
