from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
# chromedriver = "D:/Program Files (x86)/Mozilla Firefox/firefox.exe"


class NewTest(LiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Firefox(firefox_binary="D:/Program Files (x86)/Mozilla Firefox/firefox.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def testthiscase(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        self.check_for_row_in_list_table('1:Buy peacock feathers')
        # self.assertTrue(
        #     any(row.text=='1: Buy peacock feathers' for row in rows),
        #     "the table text is %s" % table.text
        # )

        self.fail('Finish')

# if __name__=='__main__':
#     unittest.main()