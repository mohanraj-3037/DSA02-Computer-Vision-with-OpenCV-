import cv2, numpy as np
img = cv2.imread("input.jpg", 0)
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharp = cv2.filter2D(img, -1, kernel)
cv2.imwrite("Laplacian_positive_center.jpg", sharp)
