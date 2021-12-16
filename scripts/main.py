from RPIclass import Camera
import RPi.GPIO as io

picam = Camera()


if __name__ == "__main__":
    picam.cool_waiting_flash()
    picam.flash_enviroment(io.HIGH)
    print('Hola! Porfavor, acerca tu imagen a la zona iluminada por la camara\n')
    name = input('Escribe el nombre del archivo final y presiona "enter" para tomar la foto\n')

    picam.capture(name)
    picam.flash_enviroment(io.LOW)

    path = picam.path
    print('Perfecto! la imagen esta guardada, revisa el archivo')
    print('En una terminal nativa copia el siguiente comando:')
    print('scp pi@gonz-zerow.local:{} path/to/location/image.jpg'.format(path))