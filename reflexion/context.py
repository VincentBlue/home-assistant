#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Context:

    def __init__(self, config):

        self.config = config
        self.log = self.config.log
        self.log.info("Loading module Context...")

        self.context = {}

    def get_attribute(self):
        pass