#!/usr/bin/env python
# -*- coding: utf-8 -*-

class EventHandler:
    def __init__(self, config):

        self.config = config
        self.log = self.config.log
        self.log.debug("Starting Event handler...")
