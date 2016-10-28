from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url='http://'+arg.split('=')[1]
                return
        super(FunctionalTest).setUpClass()
        cls.server_url=cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url ==cls.live_server_url:
            super(FunctionalTest).tearDownClass()

    def setUp(self):
        self.browser=webdriver.Firefox(firefox_binary="D:/Program Files (x86)/Mozilla Firefox/firefox.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # self.browser.refresh()
        self.browser.quit()

    def finish_init_login(self,user,passwd):
        self.browser.get(self.server_url)
        self.assertIn('Neo-CloudUltra', self.browser.title)
        self.browser.find_element_by_id('id_username').send_keys(user)
        self.browser.find_element_by_id('id_password').send_keys(passwd)
        self.browser.find_element_by_id('loginBtn').click()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])