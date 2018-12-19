from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('TO-DO', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to--do item'
        )
        inputbox.send_keys("buy a book")
        inputbox.send_keys(Keys.ENTER)
        sleep(10)
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_element_by_tag_name('tr')
        # 使用f即可使用花括号插入局部变量
        self.assertTrue(any(row.text == '1: buy a book'for row in rows), f"New to-do item did not appear in table. Contents were:\n{table.text}")
        # self.fail 都会失败，生成指定的错误信息，这里是为了提醒测试结束
        self.fail('Finish the test!')


if __name__ == '__main__':
    # warnings='ignore'参数的设置是为了禁止抛出ResourceWarning异常
    unittest.main(warnings='ignore')

