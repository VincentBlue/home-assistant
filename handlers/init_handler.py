#!/usr/bin/env python
# -*- coding: utf-8 -*-

from initialisation.configuration import *
from initialisation.initialisation import *
from initialisation.compilation import *
from initialisation.words import *

class InitHandler:
    def __init__(self):

        self.config = Configuration()
        self.load_configuration()

        print ("              ###################### Version: " + self.config.engine_version + " #######################\n")

        self.log = self.config.log
        self.log.debug("Starting Initialisation handler...")

        self.config.words  = Words()
        self.init          = Initialisation(self.config)
        self.compil        = Compilation(self.config, self.init)



        self.config.check_recognition_files()

        self.compilation()





        self.init.load_files()


    def load_configuration(self):

        self.config.check_configuration_file()
        self.config.set_configuration()
        self.config.create_log()

    def compilation(self):

        self.init.check_correct_arbo()
        self.init.check_files_changes()
        self.compil.compilation()
        self.compil.regex_convert()