'''
Created on Jul 17, 2022

@author: 16145
'''


from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO

# This one is in Main.py only
from image_functions import *


if __name__ == '__main__':
    # open an image file. The default path is where this python module is
    im = Image.open("SiriusAndViolet.jpg")
    print(im.width, im.height, im.mode, im.format)  # Display some info about the image
    
    my_image = load_image("SiriusAndViolet.jpg")
    my_image.show(my_image)
