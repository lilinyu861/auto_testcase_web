from selenium import webdriver
from time import sleep
import unittest


class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('TO-DO', self.browser.title)
        # self.fail 都会失败，生成指定的错误信息，这里是为了提醒测试结束
        self.fail('Finish the test!')


if __name__ == '__main__':
    # warnings='ignore'参数的设置是为了禁止抛出ResourceWarning异常
    unittest.main(warnings='ignore')

