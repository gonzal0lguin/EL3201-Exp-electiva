
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("Fotoholi.png", frame)
        print("Foto tomada correctamente")
        break

cap.release()

img =cv2.imread('Fotoholi.png')

cv2.destroyAllWindows()

cv2.imshow('foto', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
