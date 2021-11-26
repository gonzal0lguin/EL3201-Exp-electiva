# TODO: 'convertir todo esto a una clase con métodos:
#  1) buscar los lower bounds mediantes los sliders y que la func retorne la
#     máscara con los valores de los threshold
#  2) tomar esos valores y generar la imagen correspondiente con la firma con-
#     vertida a solo la curva
#  3) convertir la curva a svg
#  4) generar la animación del dibujo de la curva
#  5) quizás si no se usa la cámara de la RPI usar directamente la cámara de
#     opencv'


import cv2
import numpy as np


class Detector(object):
    def __init__(self):
        self.lower = 0
        self.upper = 0
        self.winname = 'Ajuste de máscara'
        self.mask = 0
        self.img = 0
        self.img_extracted = 0

    def add_img(self, path_to_img):
        initial = cv2.imread(path_to_img)
        self.img = cv2.cvtColor(initial, cv2.COLOR_BGR2HSV)
        self.img_extracted = self.img.copy()

    def nothing(self, x):
        pass

    def get_mask_bounds(self, path_to_img):
        self.add_img(path_to_img)
        cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
        cv2.createTrackbar('R', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('G', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('B', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('Ru', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('Gu', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('Bu', 'image', 0, 255, self.nothing)

        while ((cv2.waitKey(1) & 0xFF) != 27):
            r = cv2.getTrackbarPos('R', 'image')
            g = cv2.getTrackbarPos('G', 'image')
            b = cv2.getTrackbarPos('B', 'image')
            ru = cv2.getTrackbarPos('Ru', 'image')
            gu = cv2.getTrackbarPos('Gu', 'image')
            bu = cv2.getTrackbarPos('Bu', 'image')
            lower_lim = np.array([r, g, b])
            upper_lim = np.array([ru, gu, bu])

            mask = cv2.inRange(self.img, lower_lim, upper_lim)

            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
            close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

            cv2.imshow('image', close)

        cv2.destroyAllWindows()

        self.lower = lower_lim
        self.upper = upper_lim
        self.mask = close

    def get_only_curve(self):
        cnts = cv2.findContours(self.mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        boxes = []
        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            boxes.append([x, y, x + w, y + h])

        boxes = np.asarray(boxes)
        try:
            left = np.min(boxes[:, 0])
            top = np.min(boxes[:, 1])
            right = np.max(boxes[:, 2])
            bottom = np.max(boxes[:, 3])

            self.img_extracted[self.mask == 0] = (255, 255, 255)
            ROI = self.img_extracted[top:bottom, left:right].copy()
            cv2.rectangle(self.img_extracted, (left, top), (right, bottom), (36, 255, 12), 2)

            cv2.imshow('result', self.img_extracted)
            cv2.imshow('ROI', ROI)
            cv2.imshow('close', self.mask)
            # cv2.imwrite('result.png', result)
            # cv2.imwrite('ROI.png', ROI)
            cv2.waitKey()

        except:
            print('Not enough contours found')



if __name__ == "__main__":
    yay = Detector()
    yay.get_mask_bounds('firma2.png')
    print(yay.lower, yay.upper)
    yay.get_only_curve()