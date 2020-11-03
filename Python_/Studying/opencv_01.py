import cv2
cap = cv2.VideoCapture(1)
scalling_facotr = 1
while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,None,fx = scalling_facotr,fy=scalling_facotr,interpolation=cv2.INTER_AREA)
    c = cv2.imshow('webcam',frame)
    c = cv2.waitKey(1)
    if c == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()