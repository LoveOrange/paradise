#!/usr/bin/python
# -*- coding:utf-8 -*-

from .dom import Dom
from selenium import webdriver


class SeleniumUtils(object):

    def __init__(self, url):
        self._browser = webdriver.Chrome()
        self.url = url

    def jump(self, url):
        self._browser.get(url)

    def check_title(self, expect):
        self._browser.get(self.url)
        return expect == self._browser.title

    def click(self, dom):
        dom_element = Dom(dom)
        real_dom = self.get_dom_element(dom_element)
        real_dom.click()

    def fill(self, dom):
        dom_element = Dom(dom)
        fill_value = dom_element.params
        _dom = self.get_dom_element(dom_element)
        _dom.send_keys(fill_value)

    def get_dom_element(self, dom):
        if dom.type == "class":
            return self._browser.find_element_by_class_name(dom.dom)
        elif dom.type == "id":
            return self._browser.find_element_by_id(dom.dom)
        else:
            return self._browser.find_element_by_tag_name(dom.dom)

    def get(self, dom):
        dom_element = Dom(dom)
        real_dom = self.get_dom_element(dom_element)
        return real_dom.text

    def get_title(self):
        return self._browser.title

browser = None


def get_browser(url):
    global browser
    if browser is None:
        browser = SeleniumUtils(url)
    return browser
