import cv2
img = cv2.imread('img.jpg')
x,y,w,h = 100,100,200,200
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
obj = img[y:y+h, x:x+w]
cv2.imwrite("rectangle.jpg", img)
cv2.imwrite("extracted_object.jpg", obj)
