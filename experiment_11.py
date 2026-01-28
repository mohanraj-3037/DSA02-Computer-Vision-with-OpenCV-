import cv2
import numpy as np
img = cv2.imread('input.jpg')
rows, cols = img.shape[:2]
pts_src = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts_dst = np.float32([[10, 100], [180, 30], [80, 230], [230, 150]])
M, _ = cv2.findHomography(pts_src, pts_dst)
dst = cv2.warpPerspective(img, M, (cols, rows))
cv2.imwrite('dst.jpg',dst)

cv2.imshow('DLT Transformation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
