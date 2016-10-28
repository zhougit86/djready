# -*- coding:utf-8 -*-

from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

user_list={'user1':'passw0rd'}


class NewVisitorTest(FunctionalTest):
    def test_login(self):
        self.finish_init_login( user_list.keys()[0], user_list.values()[0])

        time.sleep(5)

    # def test_click_compute_host_list(self):
        self.browser.find_element_by_link_text("计算").click()
        time.sleep(1)
        list=self.browser.find_element_by_xpath("//a[@href='/project/compute/']")
        # print list.get_attribute('href')
        list.click()
        time.sleep(5)
        list=self.browser.find_element_by_id('instances').find_elements_by_tag_name('tr')
        self.browser.session_id()
        for i in list:
            print i.get_attribute('data-object-id')




