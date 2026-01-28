import cv2
img = cv2.imread("input.jpg", 0)
blur = cv2.GaussianBlur(img, (5,5), 0)
mask = cv2.subtract(img, blur)
sharp = cv2.add(img, mask)
cv2.imwrite("Unsharp_Masking.jpg", sharp)
