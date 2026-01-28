import cv2

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
assert img is not None, "Image not found!"

sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)

cv2.imwrite("Sobel_y_axis.jpg", sobel_y)

