#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os

class Compilation:

    def __init__(self, config, init):

        self.config = config
        self.log = self.config.log
        self.init = init


    def compilation(self):

        for item in self.config.compilation_filelist:
            if "sentences" in item and not "__" in item:
                self.log.info("Compiling file: " + item)

                with open(item, "r") as f:
                    content = f.readlines()

                all_specsin  = ""
                all_textin   = ""
                all_textout  = ""
                all_specsout = ""
                content = sorted(content, key=str.lower)

                buffer = [0, None]
                for sentence in content:
                    sentence = sentence[:-1]
                    specsin  = ""
                    specsout = ""

                    sentence = sentence.split("=")
                    textin   = sentence[0]
                    textout  = sentence[1]
                    if "->" in textin:
                        sentence = textin.split("->")
                        textin   = sentence[0]
                        specsin  = sentence[1]
                    if "->" in textout:
                        sentence = textout.split("->")
                        specsout = sentence[0]
                        textout  = sentence[1]

                    """if buffer[1] == textin:
                        buffer[0] += 1
                        buffer[1] = textin
                        textin = str(buffer[0]) + textin
                        
                    else:
                        buffer[0] = 0
                        buffer[1] = textin
                        textin = str(0) + textin"""

                    all_specsin  += specsin + "\n"
                    all_textin   += textin + "\n"
                    all_specsout += specsout +"\n"
                    all_textout  += textout + "\n"

                all_specsin  = all_specsin[:-1]
                all_textin   = all_textin[:-1]
                all_specsout = all_specsout[:-1]
                all_textout  = all_textout[:-1]

                (dir_only, name_only) = self.init.get_filename_only(item)

                specsin_file  = self.config.specsin_path + name_only
                textin_file   = self.config.textin_path + name_only
                specsout_file = self.config.specsout_path + name_only
                textout_file  = self.config.textout_path + name_only

                with open(specsin_file, "w") as f:
                    f.write(all_specsin)
                with open(textin_file, "w") as f:
                    f.write(all_textin)
                with open(specsout_file, "w") as f:
                    f.write(all_specsout)
                with open(textout_file, "w") as f:
                    f.write(all_textout)

                self.config.compiled_files.append(name_only)


    def regex_convert(self):
        # Convert a string in regex pattern
        #TODO: si un mot est un synonyme, alors écrire autant de nouvelles lignes correspondant

        for dirpath, dirnames, filenames in os.walk(self.config.textin_path):
            for fname in filenames:
                with open(dirpath + fname, "r") as f:
                    content = f.readlines()

                allregex = ""

                for line in content:
                    regex = ""
                    if line[0] == "|":
                        regex += "^"
                        line = line[1:]

                    for letter in line:
                        test = re.search(r"\w", letter)
                        if test is not None:
                            regex += letter

                        if letter == " ":
                            regex += letter

                        if letter == "*":
                            regex += "[ \w]*"

                    if letter == "|":
                        regex = regex + "$"

                    allregex += regex + "\n"

                with open(dirpath + fname, "w") as f:
                    # without final \n
                    f.write(allregex[:-1])
