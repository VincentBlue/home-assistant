#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.main_handler import *

if __name__ == '__main__':

    banner = """
    #################################################################################
    #                                                                               #
    #  `7MMM.     ,MMF'      db      `7MM\"""Mq.  `7MMF'  .g8""8q.   `7MN.   `7MF'   #
    #    MMMb    dPMM       ;MM:       MM   `MM.   MM  .dP'    `YM.   MMN.    M     #
    #    M YM   ,M MM      ,V^MM.      MM   ,M9    MM  dM'      `MM   M YMb   M     #
    #    M  Mb  M' MM     ,M  `MM      MMmmdM9     MM  MM        MM   M  `MN. M     #
    #    M  YM.P'  MM     AbmmmqMA     MM  YM.     MM  MM.      ,MP   M   `MM.M     #
    #    M  `YM'   MM    A'     VML    MM   `Mb.   MM  `Mb.    ,dP'   M     YMM     #
    #  .JML. `'  .JMML..AMA.   .AMMA..JMML. .JMM..JMML.  `"bmmd"'   .JML.    YM     #
    #                                                                               #
    #################################################################################
"""
    print (banner)
                
    MainHandler()

# Files architecture:

#pattern->[spec1:value;spec2:value]{func1(args):value;func2(args):value}pattern=[spec1:value;spec2:value]{func1(args);func2(args)}->pattern1[spec]|pattern2{func(args)}