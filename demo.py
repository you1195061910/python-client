#!/usr/bin/env python
#coding=utf-8

import os

from PIL import Image
from pytesseract import image_to_string

PATH = lambda p: os.path.abspath(p)
SCREEN_PATH = PATH(os.path.join(os.getcwd(), "./screen"))

def parse_string(load_image):
    fileName = PATH(SCREEN_PATH + "/" + load_image + ".png")
    img = Image.open(fileName)
    text = image_to_string(img, lang='chi_sim')
    print(text)

parse_string('element')
