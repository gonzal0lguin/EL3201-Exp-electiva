import cv2
import numpy as np
image = cv2.imread('/Users/gonzalolguin/Desktop/firma2.png')

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0


g = image.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(imgray, 50, 120)
cv2.imshow('cani', canny)


kernel = np.ones((4,4),np.float32)/16
dst = cv2.filter2D(imgray,-1,kernel)
#cv2.imshow('imgray', dst)

ret, thresh = cv2.threshold(canny, 255, 255, 255)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cv2.drawContours(image, contours, -1, (0,255,0), 2)

img_1 = np.zeros([1000,1000,1],dtype=np.uint8)
img_1.fill(255)

cv2.drawContours(img_1, contours, -1, (0,255,0), 2)

cv2.imshow('a', img_1)
#cv2.imwrite('/Users/gonzalolguin/Desktop/testlindraw.jpg', img_1)

#print(contours)

# RGB - Blue
#cv2.imshow('original', image)
# #cv2.imshow('B-RGB', b)

# # # RGB - Green
# cv2.imshow('G-RGB', g)

# # RGB - Red
#cv2.imshow('R-RGB', r)

cv2.waitKey(0)