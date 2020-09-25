import time, argparse, imageIO, log
from gauss import gaussian_blur
from sobel import edge_detector
from laplacian import sharpening

parser = argparse.ArgumentParser()
parser.add_argument('--blur', action='store_true')
parser.add_argument('--edge', action='store_true')
parser.add_argument('--sharp', action='store_true')
parser.add_argument("input_file", help="The input image file.")
parser.add_argument("output_file", help="The output image file.")
args = parser.parse_args()

img = imageIO.readImage(args.input_file)
if img is not None:
    startTime = time.time()
    log.status("proccessing image")
    if args.blur:
        blurImage = gaussian_blur(img)
        imageIO.writeImage(blurImage,args.output_file)
    elif args.edge:
        edgeImage = edge_detector(img)
        imageIO.writeImage(edgeImage,args.output_file)
    elif args.sharp:
        sharpImage = sharpening(img)
        imageIO.writeImage(sharpImage,args.output_file)