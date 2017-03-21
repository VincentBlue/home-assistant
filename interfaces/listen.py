#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr

class Listen:

    def __init__(self, config):

        self.config = config
        self.log = self.config.log
        self.log.info("Loading module Listen...")
        self.ticked = False
        self.vocal_recognition = self.config.vocal_recognition
        self.speech = sr.Recognizer()


    def listen_user(self, conversation):

        self.sentence = ""
        print("############################################")

        if self.ticked == False:
            self.sentence = self.config.assistant_name

            while True:
                if self.vocal_recognition is True:
                    self.record()
                else:
                    #Python 2
                    #self.sentence = raw_input()
                    #Python 3
                    self.sentence = input()

                if self.sentence == self.config.assistant_name or self.sentence == self.config.assistant_name.lower():
                    self.ticked = True
                    break
        else:
            if self.vocal_recognition is True:
                    self.record()
            else:
                #Python 2
                #self.sentence = raw_input()
                #Python 3
                self.sentence = input()

        conversation["input"] = self.sentence
        self.log.info(self.sentence)


    def record(self):
        
        self.log.debug("Listening...")
        with sr.Microphone() as source:
            audio = self.speech.listen(source)
        try:
            self.sentence = self.speech.recognize_google(audio, language='fr-FR', key="AIzaSyDTPx-WNlddjq0Tu7UOVm5uA3_o1lR8dPg")
            print (self.sentence)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            self.record()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))