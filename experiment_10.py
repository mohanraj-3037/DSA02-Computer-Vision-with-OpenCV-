import cv2, numpy as np
img = cv2.imread("image.jpg")
src = np.float32([[0,0],[300,0],[300,300],[0,300]])
dst = np.float32([[30,50],[270,10],[290,290],[20,280]])
H, _ = cv2.findHomography(src, dst)
cv2.imwrite("homography.jpg", cv2.warpPerspective(img,H,(300,300)))
