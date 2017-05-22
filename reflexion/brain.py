#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk.data
from nltk.corpus import stopwords
import re 

class Brain:

    def __init__(self, config, context):

        self.config = config
        self.log = self.config.log
        self.log.info("Loading module Brain...")
        self.words = self.config.words
        self.context = context


    def analyse(self, conversation):

        text_input = conversation["input"]
        self.log.debug("input = " + text_input)

        refactored_input = self.nltk_parse(text_input)
        self.log.debug("refactored = " + refactored_input)

        #print(self.words.textin)
        key = None
        for item in self.words.textin:
            #print(key[:1])
            m = re.search(item[1:], refactored_input)
            if m is not None:
                self.log.debug("Key = " + self.words.textin[item])
                key = self.words.textin[item]
                break
                # TODO: Chef if next entries have the same pattern
        else:
            self.log.warning("Unknown response")
            key = self.words.textin["000NOTFOUND"]

        self.check_dicts(key)
        self.parse_specs(self.words.specsin[key])

        self.check_attrs_funcs()

        #self.parse_specs(self.words.specsout[key])


    def check_dicts(self, key):

        if not self.words.specsin[key]:
            self.log.debug("No specsin required")
        else: self.log.debug(self.words.specsin[key])

        if not self.words.specsout[key]:
            self.log.debug("No specsout specified")
        else: self.log.debug(self.words.specsout[key])

        if not self.words.textout[key]:
            self.log.debug("No textout specified")
        else: self.log.debug(self.words.textout[key])


    def parse_specs(self, specs):

        self.words.parsed_specs["func"] = specs[specs.find("{")+1:specs.find("}")].split(";")
        self.words.parsed_specs["attr"] = specs[specs.find("[")+1:specs.find("]")].split(";")

        #self.log.error(self.words.parsed_specs["attr"])
        #self.log.error(self.words.parsed_specs["func"])


    def check_attrs_funcs(self):
        
        for element in ["func", "attr"]:
            if self.words.parsed_specs[element] != ['']:
                for item in self.words.parsed_specs[element]:
                    a = item.split(":")
                    self.log.debug("getting \"" + a[0] + "\" and ensure value is -> " + a[1])
                    if not hasattr(self.context, a[0]):
                        self.log.debug("Context has no variable -> " + a[0])
                        continue
                    elif getattr(self.context, a[0]) != "" and getattr(self.context, a[0]) != a[1]:
                        self.log.debug("\"" + a[0] + "\" value is not -> " + a[1])
                        break
                    else:
                        self.log.debug("Found \"" + a[0] + "\" -> " + a[1])
            
            #do it for func !!



    def nltk_parse(self, text):
        
        # Update the input text to simplify it

        # Remove non letters
        text = re.sub("[^a-zA-Z?]", " ", text)
        # Convert to lowercase
        text = text.lower()
        # Tokenize
        text = nltk.word_tokenize(text, "french")
        # Remove french stop words
        from nltk.corpus import stopwords
        stopwords = set(stopwords.words("french"))
        text = [word for word in text if word not in stopwords]

        textstr = " "
        textstr = textstr.join(text)
        self.log.debug(textstr)
        return textstr