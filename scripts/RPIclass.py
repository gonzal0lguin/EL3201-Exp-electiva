from time import sleep
import RPi.GPIO as io
from picamera import PiCamera


class Camera(object):
    def __init__(self):
        self.cam = PiCamera()
        self.cam.resolution = (1024, 768)
        self.pins = [26, 19, 13, 6]
        self.init_leds()
        self.path = 0

    def init_leds(self):
        """
        incializa los pines de los leds como salidas
        """

        io.setmode(io.BCM)
        io.setwarnings(False)
        for i in range(len(self.pins)):
            io.setup(self.pins[i], io.OUT, initial=io.LOW)

    def cool_waiting_flash(self):
        """
        secuencia de luces
        """

        for i in range(len(self.pins)):
            io.output(self.pins[i], io.HIGH)
            sleep(0.1)
            io.output(self.pins[i], io.LOW)
            sleep(0.3)

    def flash_enviroment(self, mode):
        """
        enciende/apaga todos los leds
        :param mode: io.HIGH, io.LOW
        """
        for i in range(len(self.pins)):
            io.output(self.pins[i], mode)

    def capture(self, name):
        """
        Toma una foto
        :param name: nombre para la foto
        """

        sleep(1)
        self.path = '/home/pi/EL3201-Exp-electiva/scripts/{}.jpg'.format(name)
        print(self.path)
        self.cam.capture(self.path)
