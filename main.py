#!/usr/bin/python
# -*- coding:utf-8 -*-

from src.config import Config
from src.case_handler import CaseHandler

CONFIG_FILE = "config.yml"

config = Config(CONFIG_FILE)
cases = CaseHandler(config).load_cases()
