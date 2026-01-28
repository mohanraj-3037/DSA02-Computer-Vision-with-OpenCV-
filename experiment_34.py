import cv2
car = cv2.CascadeClassifier('haarcascade_car.xml')
cap = cv2.VideoCapture('cars.mp4')
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cars = car.detectMultiScale(gray, 1.1, 3)
for (x,y,w,h) in cars:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imwrite("vehicle_detected.jpg", frame)
