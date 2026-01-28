import cv2
cap = cv2.VideoCapture('video.mp4')
frames = []
while cap.isOpened():
    ret, f = cap.read()
    if not ret: break
    frames.append(f)
for f in reversed(frames):
    cv2.imshow("Reverse Video", f)
    if cv2.waitKey(30) == 27: break
