#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk.data
from nltk.corpus import stopwords
import re

class Brain:

    def __init__(self, config):

        print("Loading module Brain...")

        self.config = config
        self.log = self.config.log
        self.words = self.config.words


    def analyse(self, conversation):

        text_input = conversation["input"]
        self.log.debug("input = " + text_input)

        refactored_input = self.nltk_parse(text_input)
        self.log.debug("refactored = " + refactored_input)

        print(self.words.textin)

        found = None
        for key in self.words.textin:
            m = re.search(key, refactored_input)
            if m is not None:
                found = key
                self.log.debug(self.words.textin[key])
                break
        else:
            self.log.warning("Unknown response")

        # TODO : continue brainstorming


    def nltk_parse(self, text):
        
        # Update the input text to simplify it

        # Remove non letters
        text = re.sub("[^a-zA-Z?]", " ", text)
        # Convert to lowercase
        text = text.lower()
        # Tokenize
        text = nltk.word_tokenize(text)
        # Remove french stop words
        from nltk.corpus import stopwords
        stopwords = set(stopwords.words("french"))
        text = [word for word in text if word not in stopwords]

        textstr = " "
        textstr = textstr.join(text)
        self.log.debug(textstr)
        return textstr