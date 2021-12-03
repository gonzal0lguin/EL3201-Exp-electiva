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
        self.path = "path"

    def init_leds(self):
        io.setmode(io.BCM)
        io.setwarnings(False)
        for i in range(len(self.pins)):
            io.setup(self.pins[i], io.OUT, initial=io.LOW)

    def cool_waiting_flash(self):
        for i in range(len(self.pins)):
            io.output(self.pins[i], io.HIGH)
            sleep(0.3)
            io.output(self.pins[i], io.LOW)
            sleep(0.3)

    def flash_enviroment(self, mode):        
        for i in range(len(self.pins)):
            io.output(self.pins[i], mode)

    def capture(self, name):
        self.cam.rotation = 180
        sleep(1)
        self.path = 'home/pi/Desktop/EL3201-Exp-electiva/scripts/{}.jpg'.format(name)
        self.cam.capture(self.path)

