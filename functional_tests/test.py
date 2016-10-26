from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

# chromedriver = "D:/Program Files (x86)/Mozilla Firefox/firefox.exe"


class NewVisitorTest(FunctionalTest):
    def testthiscase(self):
        self.browser.get(self.live_server_url)


        self.assertIn('To-Do',self.browser.title)
        self.assertIn('To-Do',self.browser.find_element_by_tag_name('h1').text)

        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        edith_list_url=self.browser.current_url
        self.assertRegexpMatches(edith_list_url,'/lists/.+')
        self.check_for_row_in_list_table('1:Buy peacock feathers')

        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy another feather')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_for_row_in_list_table('2:Buy another feather')
        # self.assertTrue(
        #     any(row.text=='1: Buy peacock feathers' for row in rows),
        #     "the table text is %s" % table.text
        # )

        #----------------------------another user----------
        self.browser.quit()
        self.browser = webdriver.Firefox(firefox_binary="D:/Program Files (x86)/Mozilla Firefox/firefox.exe")

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        francis_list_url = self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        #-----------------end of another user-------


        self.fail('Finish')

# if __name__=='__main__':
#     unittest.main()