import cv2, numpy as np
img = cv2.imread('img.jpg', 0)
gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
grad = cv2.convertScaleAbs(gx + gy)
sharp = cv2.add(img, grad)
cv2.imwrite("sharpened.jpg", sharp)
