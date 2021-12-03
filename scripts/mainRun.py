from time import sleep
from detectionV1 import Detector
import cv2 as cv
import linedraw

if __name__ == "__main__":
    path = input('Ingerese path completo de la foto a modificar\n')
    det = Detector(path)
    det.add_img()
    det.extract_contours()

    option = input('¿desea guardar las curvas extraídas? [y/n]')
    if option == 'y':
        path_out = input('Ingerese path completo para guardar la foto\n')
        det.save_img(path_out)
        print('Foto guardada exitosamente!')
        option2 = input('¿Desea visalizarla? [y/n] ')

        if option2 == 'y':
            lines = linedraw.sketch(path_out)
            linedraw.visualize(lines)

#/Users/gonzalolguin/Desktop/teste.jpg
#/Users/gonzalolguin/Desktop/firma2.png