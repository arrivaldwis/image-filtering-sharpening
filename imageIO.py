import imageio
from scipy import *
from PIL import Image
import numpy as np
import os, log

def readImage(filename):
    if os.path.exists(filename):
        log.status("reading from " + filename)
        imageMemmap = array(Image.open(filename).convert("L"))
        log.status("successfully read from" + filename)
        try:
            os.remove(".temp.raw")
        finally:
            return imageMemmap
        
    else:
        log.error("can't read from " + filename)
        return None

def writeImage(imageMemmap,filename):
    log.status("writing image to "+filename)
    imageio.imwrite(filename, imageMemmap)
    log.status("image successfully write to " + filename)