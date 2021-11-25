# import the necessary packages
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--Imagenes/Elprofe.jpeg", required=True,
	help="path to input image")
ap.add_argument("-c", "--connectivity", type=int, default=4,
	help="connectivity for connected component analysis")
args = vars(ap.parse_args())

# load the input image from disk, convert it to grayscale, and
# threshold it
image = cv2.imread(args["Image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cv2.imshow('imagen',image)