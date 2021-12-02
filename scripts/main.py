from scripts.RPIclass import Camera

picam = Camera()


if __name__ == "__main__":
    picam.cool_waiting_flash()
    picam.flash_enviroment(io.HIGH)
    print('Hola! Porfavor, acerca tu imagen a la zona iluminada por la camara')
    input('Presiona "enter" para tomar la foto')

    picam.capture()
    #Todo: 'aca la secuancia de toma de la foto, una vez que se obtiene se debe
    # mostrar un preview y preguntar si está bien, si no dar opciones para
    # corregir lo que esté mal'


    #### luego de que tod o este bien se uarda la imagen y se dice:
    path = picam.path
    print('Perfecto! la imagen está guardada, revisa el archivo --archivo--')
    print('En una terminal nativa copia el siguiente comando:')
    print('scp /home/pi/EL3201-Exp-electiva/scripts/photos/{} path/to/location/{}'.format(path))