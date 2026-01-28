import cv2
img = cv2.imread('img.jpg')
cv2.putText(img, "WATERMARK", (50,50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
cv2.imwrite("watermark.jpg", img)
