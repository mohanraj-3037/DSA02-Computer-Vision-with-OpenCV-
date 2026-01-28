import cv2
img = cv2.imread("image.jpg")
(h,w) = img.shape[:2]
M1 = cv2.getRotationMatrix2D((w//2,h//2), -45, 1)  # clockwise
M2 = cv2.getRotationMatrix2D((w//2,h//2), 45, 1)   # counter-clockwise
cv2.imwrite("cw.jpg", cv2.warpAffine(img,M1,(w,h)))
cv2.imwrite("ccw.jpg", cv2.warpAffine(img,M2,(w,h)))
