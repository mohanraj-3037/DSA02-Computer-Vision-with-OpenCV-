import cv2
img = cv2.imread('input.jpg')
edges = cv2.Canny(img, 100, 200)
cv2.imwrite("canny.jpg",edges)
