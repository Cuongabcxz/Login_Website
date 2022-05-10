#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BANNER = """
     ___             _         ___                    
    | _ ) _ _  _  _ | |_  ___ | __| ___  _ _  __  ___ 
    | _ \| '_|| || ||  _|/ -_)| _| / _ \| '_|/ _|/ -_)
    |___/|_|   \_._| \__|\___||_|  \___/|_|  \__|\___|
                                                                       
"""


BASEPATH = os.path.dirname(os.path.realpath(__file__+'/../..'))
DEFAULT_NB_THREADS = 10
MAX_THREADS = 50
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'
TIMEOUT = 20
MAX_ERRORS = 10

