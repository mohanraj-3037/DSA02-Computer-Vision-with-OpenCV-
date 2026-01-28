import cv2, numpy as np
img = cv2.imread("input.jpg", 0)
A = 2
kernel = np.array([[0,-1,0],[-1,A+4,-1],[0,-1,0]])
sharp = cv2.filter2D(img, -1, kernel)
cv2.imwrite("HighBoost_cross.jpg", sharp)
