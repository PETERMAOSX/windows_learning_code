import cv2
import numpy as np
cap = cv2.VideoCapture(1)
while True:
    ret,frame = cap.read()
    cv2.imshow("capture",frame)
    if cv2.waitKey(5) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
