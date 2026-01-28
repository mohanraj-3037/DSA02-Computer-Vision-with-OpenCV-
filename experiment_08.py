import cv2, numpy as np
img = cv2.imread("image.jpg")
pts1 = np.float32([[0,0],[300,0],[0,300],[300,300]])
pts2 = np.float32([[50,50],[250,0],[0,300],[300,250]])
M = cv2.getPerspectiveTransform(pts1, pts2)
cv2.imwrite("perspective.jpg", cv2.warpPerspective(img,M,(300,300)))
