import cv2, numpy as np
img = cv2.imread('img.jpg', 0)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite("opening.jpg", opening)
