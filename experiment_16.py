import cv2, numpy as np
img = cv2.imread("input.jpg", 0)
kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
lap = cv2.filter2D(img, -1, kernel)
sharp = cv2.subtract(img, lap)
cv2.imwrite("Laplacian_sharp_-4.jpg", sharp)
