import cv2
img = cv2.imread('img.jpg')
crop = img[50:200, 50:200]
img[250:400, 250:400] = crop
cv2.imwrite("copy_paste.jpg", img)
