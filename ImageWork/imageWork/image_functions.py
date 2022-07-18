'''
Created on Jul 17, 2022

@author: 16145
'''

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO

def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
    except:
        return None
    
def save_image( imageObject, outfilename ) :
    """
    Save an image to disk
    :param imageObject: The Image to save
    :param outfilename: The target file
    """
    imageObject.save( outfilename )



