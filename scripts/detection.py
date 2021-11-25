import numpy as np
import cv2

image = cv2.imread('firma2.png')
result = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_blue = np.array([20, 20, 100])
upper_blue = np.array([255,255,255])

lower_black = np.array([0, 0, 0])
upper_black = np.array([20, 50, 50])


mask = cv2.inRange(image, lower_blue, upper_blue)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

boxes = []
for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    boxes.append([x, y, x + w, y + h])

boxes = np.asarray(boxes)
try:
    left = np.min(boxes[:, 0])
    top = np.min(boxes[:, 1])
    right = np.max(boxes[:, 2])
    bottom = np.max(boxes[:, 3])

    result[close == 0] = (255, 255, 255)
    ROI = result[top:bottom, left:right].copy()
    cv2.rectangle(result, (left, top), (right, bottom), (36, 255, 12), 2)

    cv2.imshow('result', result)
    cv2.imshow('ROI', ROI)
    cv2.imshow('close', close)
    # cv2.imwrite('result.png', result)
    # cv2.imwrite('ROI.png', ROI)
    cv2.waitKey()

except:
    print('Not enough contours found')

