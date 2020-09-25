import imageIO
from scipy import *
from scipy import signal

def gaussian_blur(image):
    kernel = [[1, 2, 1],
            [2, 4, 2],
            [1, 2, 1]]

    im = signal.convolve(image, kernel, mode='same')

    print (im)

    return im
