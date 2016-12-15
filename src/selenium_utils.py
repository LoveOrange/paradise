#!/usr/bin/python
# -*- coding:utf-8 -*-

from selenium import webdriver


class SeleniumUtils(object):

    def __init__(self, url):
        self._browser = webdriver.Chrome()
        self._browser.get(url)

    def check_title(self, expect):
        self._browser.get("https://github.com")
        return expect == self._browser.title

    def click(self, dom):
        real_dom = self._browser.find_element_by_class_name(dom)
        real_dom.click()

    def fill(self, dom):
        real_dom = self._browser.find_element_by_class_name(dom)
        real_dom.send_keys("LoveOrange")

    def get(self, dom):
        real_dom = self._browser.find_element_by_class_name(dom)
        return real_dom.text

    def get_title(self):
        return self._browser.title

browser = None


def get_browser():
    global browser
    if browser is None:
        browser = SeleniumUtils("https://baidu.com")
    return browser
