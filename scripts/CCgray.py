from detectionV1 import Detector

path = '/Users/gonzalolguin/Desktop/image0.jpg'
savepath = '/Users/gonzalolguin/Desktop/fotosextraidas/'
a = Detector(path)
a.add_img()
a.extract_contours()
a.show_imgs()