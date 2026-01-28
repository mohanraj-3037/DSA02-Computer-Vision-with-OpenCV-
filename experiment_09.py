import cv2, numpy as np
cap = cv2.VideoCapture("video.mp4")
M = cv2.getPerspectiveTransform(np.float32([[0,0],[640,0],[0,480],[640,480]]),
                                np.float32([[50,50],[590,0],[0,430],[640,480]]))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow("Warped", cv2.warpPerspective(frame,M,(640,480)))
    if cv2.waitKey(1)==27: break
cap.release(); cv2.destroyAllWindows()
