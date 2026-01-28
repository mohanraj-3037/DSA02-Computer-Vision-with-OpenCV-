import cv2, numpy as np
img = cv2.imread('img.jpg', 0)
kernel = np.ones((5,5), np.uint8)
eroded = cv2.erode(img, kernel, iterations=1)
cv2.imwrite("erosion.jpg", eroded)
