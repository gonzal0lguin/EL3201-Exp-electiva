from time import sleep
import RPi.GPIO as io
from picamera import PiCamera

class Camera(object):
    def __init__(self):
        self.cam = PiCamera()
        self.cam.resolution = (1024, 768)

    def flash_enviroment(self):
        # TODO: 'inicializar luces led que iluminen el ambiente para que las
        #  fotos sean consistentes y haya la menor cantidad de errores'

        pass

    def capture(self):
        # TODO: 'secuencia de captura de la foto y guardado, primero se
        #  ilumina el mabiente y luego se procede con la foto'

        self.flash_enviroment()
        pass
