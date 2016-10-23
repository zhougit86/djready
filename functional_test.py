from selenium import webdriver
import unittest
# chromedriver = "D:/Program Files (x86)/Mozilla Firefox/firefox.exe"


class NewTest(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Firefox(firefox_binary="D:/Program Files (x86)/Mozilla Firefox/firefox.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def testthiscase(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Django',self.browser.title)
        # self.fail('Finish')

if __name__=='__main__':
    unittest.main()