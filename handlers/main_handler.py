#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.init_handler import *
from handlers.life_handler import *
from handlers.event_handler import *

class MainHandler:
    def __init__(self):

        self.init_handler = InitHandler()

        self.config = self.init_handler.config
        self.log = self.config.log

        self.log.debug("Starting Main handler...")

        
        self.life_handler = LifeHandler(self.config)       
        self.event_handler = EventHandler(self.config)

        self.development()

        self.main_loop()


    def main_loop(self):

        while True:
            self.life_handler.manage()


    def development(self):

        print("\n#####DEVELOPEMENT#####\n")





        #except(KeyboardInterrupt, EOFError, SystemExit):
            #break

        print("\n#####DEVELOPEMENT#####\n")