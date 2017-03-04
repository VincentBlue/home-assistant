#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LifeHandler:
    def __init__(self, config):

        self.config = config
        self.log = self.config.log
        self.log.debug("Starting Life handler...")


    def load_modules(self):
        
        self.listen = Listen(self.log)
        self.brain = Brain(self.log)
        self.say = Say(self.log)
