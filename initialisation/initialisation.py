#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from datetime import *
import logging
from logging.handlers import RotatingFileHandler
import configparser
import hashlib


class Initialisation:

    def __init__(self, config):

        self.config = config
        self.log = self.config.log
        self.words = self.config.words

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
                #for dev
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

        for fname in self.config.compiled_files:
            for state in self.config.compiled_states:
                self.log.debug("Loading file " + fname + " - " + state)
                with open (self.config.compiled_path + state + "/" + fname, "r") as f:
                    content = f.readlines()
                    i = 0
                    for line in content:
                        i += 1
                        if line[-1:] == '\n':
                            line = line[:-1]
                        # Wanted : unique question --> key to look for
                        if state == self.config.textin_part:
                            cpt = self.check_key_existence(self.words.textin, line, 0)
                            self.words.textin[str(cpt) + line] = fname + "-" + str(i)
                        elif state == self.config.specsin_part:
                            self.words.specsin[fname + "-" + str(i)] = line
                        elif state == self.config.specsout_part:
                            self.words.specsout[fname + "-" + str(i)] = line
                        elif state == self.config.textout_part:
                            self.words.textout[fname + "-" + str(i)] = line
                    #print(content)
                    #print(self.words.specsin)
                    #print("##############################")
                    #self.words.specsin.extend
                    #print (self.words.textin)

    def check_key_existence(self, dict, key, cpt):
        if str(cpt) + key in dict:
            cpt = self.check_key_existence(dict, key, cpt+1)
        return cpt
