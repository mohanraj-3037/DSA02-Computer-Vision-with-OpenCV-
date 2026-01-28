import cv2, numpy as np
img = cv2.imread('img.jpg', 0)
kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
boundary = cv2.filter2D(img, -1, kernel)
cv2.imwrite("boundary.jpg", boundary)
