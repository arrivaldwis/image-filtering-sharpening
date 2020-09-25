import imageIO
from scipy import *
from scipy import signal
import math

def edge_detector(image):
    kernelX = [[-1, 0, 1],
    [-2, 0, 1],
    [-1, 0, 1]]

    kernelY = [[-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]]

    imX = signal.convolve(image, kernelX, mode='same')
    imY = signal.convolve(image, kernelY, mode='same')

    imageIO.writeImage(imX,'output/imX.jpeg')
    imageIO.writeImage(imY,'output/imY.jpeg')

    imFinal = sqrt(imX*imX + imY*imY)

    return imFinal