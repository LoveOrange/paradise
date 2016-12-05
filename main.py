#!/usr/bin/python
# -*- coding:utf-8 -*-

from src.config import Config
from src.case_handler import CaseHandler
from src.runner import start_test

CONFIG_FILE = "config.yml"


def main():
    config = Config(CONFIG_FILE)
    cases = CaseHandler(config).load_cases()
    start_test(cases)

if __name__ == '__main__':
    main()
