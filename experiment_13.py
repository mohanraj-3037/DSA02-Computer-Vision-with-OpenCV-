import cv2

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
assert img is not None, "Image not found!"

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)

cv2.imwrite("Sobel_x_axis.jpg", sobel_x)
