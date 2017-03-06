#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interfaces.listen import Listen
from interfaces.say import Say
from reflexion.brain import Brain

class LifeHandler:
    def __init__(self, config):

        self.config = config
        self.log = self.config.log
        self.log.debug("Starting Life handler...")

        self.conversation = {}
        self.conversation["input"] = None
        self.conversation["speak"] = None
        self.conversation["write"] = None
        self.conversation["voice"] = None

        self.load_modules()


    def load_modules(self):
        
        self.listen = Listen(self.config)
        self.brain = Brain(self.config)
        self.say = Say(self.config)


    def manage(self):

        self.conversation["input"] = None
        self.conversation["speak"] = None
        self.conversation["write"] = None
        self.conversation["voice"] = None

        self.listen.listen_user(self.conversation)
        self.brain.analyse(self.conversation)
        self.say.say_to_user(self.conversation)