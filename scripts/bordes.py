

import cv2
import numpy as np


def ordenar_puntos(puntos):
	n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()

	y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])

	x1_order = y_order[:2]
	x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])

	x2_order = y_order[2:4]
	x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])
	
	return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]
	


image = cv2.imread('Imagenes/Elprofe.jpeg')
import numpy as np
import cv2

#cv2.namedWindow("Nombre huehuehue", cv2.WINDOW_NORMAL)
#cv2.imshow("imagen", img)
#cv2.waitKey(0)

print(image.shape)

x1 = 00
x2 = 120
y1 = 20
y2 = 270
image = image[x1:x2, y1:y2, :]
cv2.imshow('frame', image)
cv2.waitKey(0)
cv2.imwrite('foto.png', image)

color = [0, 0, 0] 
#cv2.imshow('img',image)

top, bottom, left, right = [10]*4
image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
#cv2.imshow('image',image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
#cv2.imshow('image', image)
cv2.imshow('canny',canny)

cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
cnts = sorted(cnts, key=cv2.contourArea, hull = cv2.convexHull(cnts), reverse=True)[:1]
cv2.drawContours(image, cnts, 0, (0,255,255),2)##Este imprime
for c in cnts:
	epsilon = 0.05*cv2.arcLength(c,True)
	approx = cv2.approxPolyDP(c,epsilon,True)
	#print('approx=',approx)
	if len(approx)==4:
		cv2.drawContours(image, [approx], 0, (0,0,255),2)
		#cv2.imshow('image',image)
		puntos = ordenar_puntos(approx)

		cv2.circle(image, tuple(puntos[0]), 7, (255,0,0), 2)
		cv2.circle(image, tuple(puntos[1]), 7, (0,255,0), 2)
		cv2.circle(image, tuple(puntos[2]), 7, (0,0,255), 2)
		cv2.circle(image, tuple(puntos[3]), 7, (255,255,0), 2)
		
		pts1 = np.float32(puntos)
		pts2 = np.float32([[0,0],[270,0],[0,310],[270,310]])
		M = cv2.getPerspectiveTransform(pts1,pts2)
		dst = cv2.warpPerspective(gray,M,(270,310))
		#cv2.imshow('dst', dst)
cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()