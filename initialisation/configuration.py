#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import configparser
import logging

class Configuration:

    def __init__(self):

        configuration_file = "configuration.ini"
        self.configuration_file = os.path.dirname(os.path.realpath(__file__)) + "/" + configuration_file

    
    def check_configuration_file(self):

        if not os.path.isfile(self.configuration_file):
            raise Exception("Cannot find configuration file: " + self.configuration_file)


    def set_configuration(self):

        config = configparser.ConfigParser()
        config.sections()

        config.read(self.configuration_file)

        

        self.engine_version = config["DEFAULT"]["engine_version"]
        #print ("Engine version: " + engine_version + "\n\n")
        self.loglevel = config["DEFAULT"]["log_level"]


        self.vocal_recognition = config["Interfaces"].getboolean("vocal_recognition")
        self.vocal_synthesis = config["Interfaces"].getboolean("vocal_synthesis")

        self.root_recognition_path   = config["Path"]["root_recognition"]
        self.root_memory_path        = config["Path"]["root_memory"]
        self.synonyms_path           = config["Path"]["recognition.synonyms"]
        self.sentences_path          = config["Path"]["recognition.sentences"]

        self.compiled_path           = config["Path"]["recognition.compiled"]
        self.checksums_path          = config["Path"]["recognitions.checksums"]
        self.specsin_path            = config["Path"]["recognition.specsin"]
        self.textin_path             = config["Path"]["recognition.textin"]
        self.specsout_path           = config["Path"]["recognition.specsout"]
        self.textout_path            = config["Path"]["recognition.textout"]

        self.specsin_part            = config["Path"]["specsin"]
        self.textin_part             = config["Path"]["textin"]
        self.specsout_part           = config["Path"]["specsout"]
        self.textout_part            = config["Path"]["textout"]
        self.compiled_states         = [self.specsin_part,
                                        self.textin_part,
                                        self.specsout_part,
                                        self.textout_part]


        self.items_to_load           = config["Path"]["items_to_load"].split(", ")


        self.compilation_filelist = []
        self.compiled_files = []

        self.default_voice = config["Load"]["default_voice"]

        self.assistant_name = config["Load"]["assistant_name"]


    def create_log(self):

        # création de l'objet log
        self.log = logging.getLogger("my_log")
        logging.getLogger("my_log").propagate = False
        # niveau du log
        logging.getLogger("my_log").setLevel(self.loglevel)
        # Création d'unhangler de logs sur console
        stream_handler = logging.StreamHandler()        
        # Formattage de la sortie
        levelname = "%(levelname)-8s"
        filename  = "%(filename)-20s"
        fileno    = "%(lineno)-4d"
        funcname  = "%(funcName)-25s"
        message   = "%(message)s"

        formatter = logging.Formatter(levelname + " -- " + filename + fileno + " - " + funcname + " --> " + message)
        stream_handler.setFormatter(formatter)
        self.log.addHandler(stream_handler)


    def check_recognition_files(self):

        self.recognition_filelist = []
        for dirpath, dirnames, filenames in os.walk(self.root_recognition_path):
            for filename in filenames:
                self.recognition_filelist.append(os.path.join(dirpath, filename))
            if "compiled" in dirnames:
                dirnames.remove("compiled")
        
        for filename in self.recognition_filelist:
            if "__init__.py" in filename:
                self.recognition_filelist.remove(filename)
        
        for filename in self.recognition_filelist:
            self.log.debug("Found file: " + filename)