#!/usr/bin/python
# -*- coding:utf-8 -*-

import yaml


def load_config(config_file):
    with open(config_file) as config_content:
        return yaml.safe_load(config_content.read())


def get_host(config):
    if "host" in config:
        return config["host"]


def get_case_files(config):
    _case_files = []
    if "case_files" in config:
        for case_file in config["case_files"]:
            _case_files.append(case_file)
    return _case_files


class Config(object):
    """
    Config
    """
    def __init__(self, config_file):
        config = load_config(config_file)
        self.host = get_host(config)
        self.case_files = get_case_files(config)
