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

        """self.print_content(self.config.words.textin)
        self.print_content(self.config.words.specsin)
        self.print_content(self.config.words.specsout)
        self.print_content(self.config.words.textout)"""

        #except(KeyboardInterrupt, EOFError, SystemExit):
            #break

        print("\n#####DEVELOPEMENT#####\n")

    #dev
    def print_content(self, dict):
        print("#############################")
        for key in dict:
            print(key)