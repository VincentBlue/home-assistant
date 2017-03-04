#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Module de chargement des tableaux de comparaison

import os
import time
from datetime import *
import logging
from logging.handlers import RotatingFileHandler
import configparser
import hashlib


"""from initialisation.handler import *
from initialisation.regex import *
from reflexion.brain import *
from interface.listen import *
from interface.say import *"""


class Initialisation:

    def __init__(self, config, words):

        self.config = config
        self.log = self.config.log
        self.words = words

        return

        self.response = {}
        self.response["speak"] = ""
        self.response["write"] = None
        self.response["voice"] = "Michel"

        self.development()

        self.create_log()
        self.load_modules()
        self.load_files()
        self.load_memory()
        self.load_time()
        
        self.final_loading()

        self.response["speak"] = "Bonjour !"
        self.response["voice"] = "Marion"

        self.development()

        self.handler()

    def check_correct_arbo(self):
        if not os.path.exists(self.config.compiled_path):
            os.makedirs(self.config.compiled_path)
            os.makedirs(self.config.checksums_path)
            os.makedirs(self.config.specsin_path)
            os.makedirs(self.config.textin_path)
            os.makedirs(self.config.specsout_path)
            os.makedirs(self.config.textout_path)



    def check_files_changes(self):
        # Vérification des changements des fichiers

        for fname in self.config.recognition_filelist:

            (dir_only, name_only) = self.get_filename_only(fname)

            self.log.info("Checking changes in file: " + fname)
            hash_md5 = hashlib.md5()
            with open(fname, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)     
            try:
                with open(self.config.checksums_path + "checksum_" + name_only, "r") as f:
                    old_hashsum = f.read()
            except FileNotFoundError:
                with open(self.config.checksums_path + "checksum_" + name_only, "w") as f:
                    f.write("")
                old_hashsum = ""

            new_hashsum = hash_md5.hexdigest()
            self.log.debug("Old hashsum: " + old_hashsum)
            self.log.debug("New hashsum: " + new_hashsum)

            expected_line = new_hashsum
            if expected_line in old_hashsum:
                self.log.info("No changes found")
                continue

            with open(self.config.checksums_path + "checksum_" + name_only, "w") as f:
                #f.write(new_hashsum)
                self.log.info("Changes found")
                self.config.compilation_filelist.append(fname)
                continue


    def get_filename_only(self, fname):
        
        try:
            last = fname.rindex("/")
        except ValueError:
            last = fname.rindex("\\")

        name_only = fname[last+1:]
        dir_only = fname[:last+1]
        if ".txt" in name_only:
            name_only = name_only[:-4]

        return (dir_only, name_only)


    def load_files(self):
        
        print(self.config.compiled_files)

        for fname in self.config.compiled_files:
            for state in self.config.compiled_states:
                with open (self.config.compiled_path + state + "/" + fname, "r") as f:
                    content = f.readlines()
                    i = 0
                    for line in content:
                        i += 1
                        # Wanted : unique question --> key to look for
                        if state == self.config.specsin_part:
                            self.words.specsin[line] = fname + "-" + str(i)
                        elif state == self.config.textin_part:
                            self.words.textin[line] = fname + "-" + str(i)
                        elif state == self.config.specsout_part:
                            self.words.specsin[fname + "-" + str(i)] = line
                        elif state == self.config.textout_part:
                            self.words.textout[fname + "-" + str(i)] = line
                    print(content)
                    print (self.words.specsin)
                    print("##############################")
                    #self.words.specsin.extend

                #deeeeeev











    def load_file(self):

        files_to_load = os.path.listdir(self.config.sentences_path)

        print (files_to_load)
        
        self.list_items = []
        self.index_items = []

        for item in self.items_to_load:

            #print(self.check_changes(item))

            if self.check_changes(item) is True:
                self.compile(item)

            self.load_item(self.sentences_path, item)

        self.brain.init_dictionnaries(self.index_items, self.list_items)

        #print(self.list_items)

        #self.say.handler("Chargement des parametres de psychologie sociale", "Chargement des paramètres de psychologie sociale", "Michel")
        self.response["speak"] = "Ajustement des paramètres de psychologie sociale"
        #self.say.handler(self.response)
        print()
        #time.sleep(1)


    def load_item(self, path, item):

        print ("Loading file " + item + "...")

        item_content = {}
        index_content = []

        file = open(path + item + ".txt", "r", encoding='utf-8', errors='ignore')
        for line in file:

            if not "=" in line:
                raise Exception("Bad file encryption")

            line = line.split("=")
            key = self.regex.convert(line[0])

            item_content[key] = line[1]
            index_content.append(key)

        self.list_items.append((item, item_content))
        self.index_items.append((item, index_content))

    
    def load_memory(self):

        #self.say.handler("Lecture des enregistrements de la maimoire profonde", "Lecture des enregistrements de la mémoire profonde", "Michel")
        self.response["speak"] = "Lecture des enregistrements de la mémoire profonde"
        #self.say.handler(self.response)
        print()
        #time.sleep(1)

    
    def load_time(self):

        day = datetime.now()
        self.newdate = day.date()

        #self.say.handler("Raicupairation des reperes temporels", "Récupération des repères temporels", "Michel")
        self.response["speak"] = "Récupération des repères temporels"
        #self.say.handler(self.response)
        print()
        #time.sleep(1)

    
    def final_loading(self):

        self.controller = Handler(self.listen, self.brain, self.say)

        #self.say.handler("Demarrage imminent", "Démmarage imminent", "Michel")
        self.response["speak"] = "Démarrage imminent"
        #self.say.handler(self.response)
        print()
        #time.sleep(1)


    def handler(self):

        while True:
            if datetime.now().date() > self.newdate:
                self.newdate = datetime.now.date()
                self.load_files()

            self.controller.handler()

            if not self.controller.handler():
                return
