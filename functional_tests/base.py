# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys

# class NewTest(LiveServerTestCase):
class FunctionalTest(StaticLiveServerTestCase):

    # @classmethod
    # def setUpClass(cls):
    #     for arg in sys.argv:
    #         if 'liveserver' in arg:
    #             cls.server_url='http://'+arg.split('=')[1]
    #             return
    #     super(NewVisitorTest).setUpClass()
    #     cls.server_url=cls.live_server_url
    #
    # @classmethod
    # def tearDownClass(cls):
    #     if cls.server_url ==cls.live_server_url:
    #         super(NewVisitorTest).tearDownClass()

    def setUp(self):
        self.browser=webdriver.Firefox(firefox_binary="D:/Program Files (x86)/Mozilla Firefox/firefox.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # self.browser.refresh()
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

