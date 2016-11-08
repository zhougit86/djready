# -*- coding:utf-8 -*-

from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

user_list={'admin':'1qazxsw2)('}


class NewVisitorTest(FunctionalTest):
    def test_login(self):
        self.finish_init_login( user_list.keys()[0], user_list.values()[0])

        time.sleep(5)

    # def test_click_compute_host_list(self):
    #     self.browser.find_element_by_link_text("计算").click()
    #     time.sleep(1)
    #     button=self.browser.find_element_by_xpath("//a[@href='/platformenterprise']")
    #     # print list.get_attribute('href')
    #     button.click()
    #     time.sleep(8)
    #     self.create_depart()


        # def expand(nodes):
        #     for i in nodes:
        #         child = i.find_element_by_xpath("//i[@role='presentation']")
        #         print i.get_attribute('aria-expanded')
        #         child.click()
        #         time.sleep(2)
        #         node_in = self.browser.find_elements_by_xpath("//li[@aria-expanded='false']")
        #         expand(node_in)
        #
        #
        # expand(self.browser.find_elements_by_xpath("//li[@aria-expanded='false']"))
        # print self.browser.find_element_by_link_text("总部").get_attribute('id')
        # ActionChains(self.browser).double_click(self.browser.find_element_by_link_text("总部")).perform()
        # time.sleep(1)
        # ActionChains(self.browser).move_to_element(self.browser.find_element_by_link_text("PMO")).perform()
        # ActionChains(self.browser).double_click(self.browser.find_element_by_link_text("PMO")).perform()
        # time.sleep(1)













