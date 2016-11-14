#!/usr/bin/python
#  -*- coding: utf-8 -*-

from src.case_handler import *
from src.api_case_handler import *
from src.action_handler import *


def main():
    case_handler = CaseHandler()
    api_cases = case_handler.return_api_cases()
    base_config = case_handler.return_base_config()

    api_case_handler = ApiCaseHandler(base_config["host"], api_cases)
    api_case_handler.run_test()

    action_handler = ActionHandler()


if __name__ == '__main__':
    main()
