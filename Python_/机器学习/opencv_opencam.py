import cv2
cap = cv2.VideoCapture(1)
while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,None,fx=2,fy=2,interpolation=cv2.INTER_AREA)
    cv2.imshow('frame',frame)
    c = cv2.waitKey(1)
    if c == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()