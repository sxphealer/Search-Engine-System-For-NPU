# -*- coding: utf-8 -*-

import os

def get_sourcedir():
    file_dir = os.path.split(os.path.realpath(__file__))[0]
    return  file_dir

