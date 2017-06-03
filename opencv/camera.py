import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

def canny(image):
    return cv2.Canny(image, 160, 360)

def color_filter(image):    
    mask_white = cv2.inRange(image,  np.array([200,200,200]), np.array([255,255,255]))
    image_white = cv2.bitwise_and(image, image, mask=mask_white)
    image_combined = cv2.addWeighted(image_white, 1.0, image, 1.0, 0)
    return image_combined    

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_small = cv2.resize(gray, (640, 480))
    canned = canny(gray_small)
    cv2.imshow('image', canned)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()