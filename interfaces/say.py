#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
#Python 2
#import urllib2
#Python 3
import urllib.request
import urllib.parse
import pyglet
import eyed3

# Sounds : https://notificationsounds.com/

class Say:
    def __init__(self, config):
        
        self.config = config
        self.log = self.config.log
        self.log.info("Loading module Say...")
        self.vocal_synthesis = self.config.vocal_synthesis


    def say_to_user(self, conversation):

        self.voice = conversation["voice"]
        if self.voice is None :
            self.voice = self.config.default_voice

        self.text_spoken = conversation["speak"]
        text_written = self.text_spoken
        if conversation["write"] is not None:
            text_written = conversation["write"]

        # user interface
        print(text_written)
        self.log.info(text_written)

        if self.vocal_synthesis is True:
            self.log.info(self.text_spoken)
            self.generate_sound()
            self.play_sound()


    def generate_sound(self):

        data = {}
        data["method"] = "redirect"
        data["text"] = self.text_spoken
        data["voice"] = self.voice
        data["ts"] = "1421843312666"
        
        url_values = urllib.parse.urlencode(data) 
        url = "http://voxygen.fr/sites/all/modules/voxygen_voices/assets/proxy/index.php?" + url_values
        self.log.debug("trying to reach : " + url)
        
        #Python 2
        #response = urllib2.urlopen(url)
        #Python 3
        response = urllib.request.urlopen(url)

        # TODO: read the response without saving it in a file
        self.sound = response.read()

        
    def play_sound(self):

        mpname = "record"
        with open(mpname, "wb") as f:
            f.write(self.sound)
        duration = eyed3.load(mpname).info.time_secs
        song = pyglet.media.load(mpname)
        song.play()

        while time.sleep(duration):
            pyglet.app.run()
            

    