from time import sleep
import RPi.GPIO as io
from RPi.GPIO import LOW, HIGH
from picamera import PiCamera

class Camera(object):
    def __init__(self):
        self.cam = PiCamera()
        self.cam.resolution = (1024, 768)
        self.pins = [26, 19, 13, 6]
        self.init_leds()

    def init_leds(self):
        io.setmode(io.BCM)
        io.setwarnings(False)
        for i in range(len(self.pins)):
            io.setup(pins[i], io.OUT, initial=io.LOW)

    def cool_waiting_flash(self):
        for i in range(len(pins)):)
            io.output(pins[i], io.HIGH)
            sleep(0.3)
            io.output(pins[i], io.LOW)
            sleep(0.3)

    def flash_enviroment(self):
        # TODO: 'inicializar luces led que iluminen el ambiente para que las
        #  fotos sean consistentes y haya la menor cantidad de errores'

        pass

    def capture(self):
        # TODO: 'secuencia de captura de la foto y guardado'
        pass


cam = Camera()
cam.cool_waiting_flash






# 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