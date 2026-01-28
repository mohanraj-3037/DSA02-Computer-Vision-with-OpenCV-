import cv2

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
assert img is not None, "Image not found!"
sx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_xy = cv2.convertScaleAbs(cv2.magnitude(sx, sy))
cv2.imwrite("Sobel_xy_axis.jpg", sobel_xy)

