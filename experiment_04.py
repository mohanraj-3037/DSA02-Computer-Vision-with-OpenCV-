import cv2
img = cv2.imread("image.jpg")
big = cv2.resize(img, None, fx=2, fy=2)
small = cv2.resize(img, None, fx=0.5, fy=0.5)
cv2.imwrite("big.jpg", big); cv2.imwrite("small.jpg", small)
