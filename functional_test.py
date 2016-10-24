from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
# chromedriver = "D:/Program Files (x86)/Mozilla Firefox/firefox.exe"


class NewTest(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Firefox(firefox_binary="D:/Program Files (x86)/Mozilla Firefox/firefox.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def testthiscase(self):
        self.browser.get("http://localhost:8000")
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
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text=='1: Buy peacock feathers' for row in rows),
        #     "the table text is %s" % table.text
        # )
        self.assertIn('1:Buy peacock feathers', [row.text for row in rows])


        self.fail('Finish')

if __name__=='__main__':
    unittest.main()