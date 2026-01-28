import cv2, numpy as np
img = cv2.imread("image.jpg")
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1, pts2)
cv2.imwrite("affine.jpg", cv2.warpAffine(img,M,(300,300)))
