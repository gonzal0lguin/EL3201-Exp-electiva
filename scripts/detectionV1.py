import numpy as np
import cv2 as cv


class Detector(object):

    def __init__(self, path):
        self.input_path = path
        self.img = 0
        self.imgray = 0
        self.canny = 0
        self.contour = 0
        self.bkg = 0

    def add_img(self):
        """
        Lee la imagen especificada en el path al inicializar
        """

        img = cv.imread(self.input_path)
        self.img = img

    def generate_bkg(self):
        """
        genera un fondo blanco de las mismas dimensiones que self.img
        """
        height, width = self.img.shape[:2]
        self.bkg = np.zeros([height, width, 1], dtype=np.uint8)
        self.bkg.fill(255)

    def extract_contours(self):
        """
        Extrae contornos de self.img y los escribe en un fondo blanco de las
        mismas dimensiones
        """

        kernel = np.ones((3, 3), np.float32) / 9  # aplicamos un blur sutil
        blurred = cv.filter2D(self.img, -1, kernel)
        self.imgray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)  # convertimos a escala de grises
        self.canny = cv.Canny(self.imgray, 50, 120)  # deteccion canny
        ret, thresh = cv.threshold(self.canny, 255, 255, 255)
        self.contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE,
                                                   cv.CHAIN_APPROX_SIMPLE)

        self.generate_bkg()
        cv.drawContours(self.bkg, self.contours, -1, (0, 0, 0), 3)  # dibujar los contornos en un fondo blanco

        print('Imagen convertida exitosamente')

    def show_imgs(self):
        """
        Muestra todas las imagenes
        """

        cv.imshow('Original', self.img)
        cv.imshow('Gray scale', self.imgray)
        cv.imshow('Edges (canny)', self.canny)
        cv.imshow('Contours', self.bkg)

        cv.waitKey(0)  # espera a que se presione una tecla
        cv.destroyAllWindows()

    def save_img(self, path):
        """
        Guarda solamente la imagen final
        :param path: path absoluto a la imagen
        """

        cv.imwrite(path, self.bkg)  # escribe la imagen

    def save_all(self, path):
        """
        Guarda todas la imagenes
        :param path: Pat completo para las imagenes
        """

        cv.imwrite(path + 'gray4.jpg', self.imgray)
        cv.imwrite(path + 'canny4.jpg', self.canny)
        cv.imwrite(path + 'contours4.jpg', self.bkg)
