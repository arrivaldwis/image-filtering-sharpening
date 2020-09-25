import imageIO
from scipy import *
from scipy import signal

def sharpening(image):
    kernel = [[-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]]

    im = signal.convolve(image, kernel, mode='same')

    print (im)

    return im
