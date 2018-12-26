from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest


class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_tag_name("id_list_table")
        rows = table.find_element_by_tag_name("tr")
        self.assertIn(row_text, [row_text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('TO-DO', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('TO-DO', header_text)
        # buy a book
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("buy a book")
        inputbox.send_keys(Keys.ENTER)
        sleep(2)
        self.check_for_row_in_list_table("1: buy a book")
        # read book
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("read a book")
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("2: read a book")
        sleep(2)
        # self.fail 都会失败，生成指定的错误信息，这里是为了提醒测试结束
        self.fail('Finish the test!')


if __name__ == '__main__':
    # warnings='ignore'参数的设置是为了禁止抛出ResourceWarning异常
    unittest.main(warnings='ignore')

