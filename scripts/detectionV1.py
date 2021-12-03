import numpy as np
import cv2 as cv
import linedraw


class Detector(object):

    def __init__(self, path):
        self.input_path = path
        self.img = 0
        self.imgray = 0
        self.canny = 0
        self.contour = 0
        self.bkg = 0

    def add_img(self):
        img = cv.imread(self.input_path)
        if img.all() == None:
            print('Lo siento, path incorrecto.')
        else:
            self.img = img

    def generate_bkg(self):
        height, width = self.img.shape[:2]
        self.bkg = np.zeros([height, width, 1], dtype=np.uint8)
        self.bkg.fill(255)

    def extract_contours(self):
        kernel = np.ones((4, 4), np.float32) / 16  # aplicamos un blur sutil
        blurred = cv.filter2D(self.img, -1, kernel)
        self.imgray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
        self.canny = cv.Canny(self.imgray, 50, 120)
        ret, thresh = cv.threshold(self.canny, 255, 255, 255)
        self.contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE,
                                                   cv.CHAIN_APPROX_SIMPLE)

        self.generate_bkg()
        cv.drawContours(self.bkg, self.contours, -1, (0, 0, 0), 1)

        print('Imagen convertida exitosamente')



    def show_imgs(self):
        cv.imshow('Original', self.img)
        cv.imshow('Gray scale', self.imgray)
        cv.imshow('Edges (canny)', self.canny)
        cv.imshow('Contours', self.bkg)

        #cv.waitKey(0)
        #cv.destroyAllWindows()

    def save_img(self, path):
        cv.imwrite(path, self.bkg)

