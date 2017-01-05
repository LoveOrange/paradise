#!/usr/bin/python
# -*- coding:utf-8 -*-

from dom import Dom
from selenium import webdriver


class SeleniumUtils(object):

    def __init__(self):
        self._browser = webdriver.Chrome()

    def check_title(self, expect):
        self._browser.get("https://github.com")
        return expect == self._browser.title

    def click(self, dom):
        self._browser.get("https://baidu.com")

    def fill(self, dom):
        dom_element = Dom(dom)
        fill_value = dom.params
        _dom = self.get_dom_element(dom_element)
        _dom.send_keys(fill_value)

    def get_dom_element(self, dom):
        if dom.type == "class":
            return self._browser.find_element_by_class_name(dom.dom)
        elif dom.type == "id":
            return self._browser.find_element_by_id(dom.dom)
        else:
            return self._browser.find_element_by_tag_name(dom.dom)


browser = None


def get_browser():
    global browser
    if browser is None:
        browser = SeleniumUtils()
    return browser
