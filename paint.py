from this import s
import cv2
import numpy as np

drawing=False
clean=False

def nothing(x):
    pass

def brush(event,x,y,flags,param):
    global clean,drawing,r,g,b,s
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.circle(feild,(x,y),s,(b,g,r),-1,cv2.LINE_AA)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False            
    if event==cv2.EVENT_RBUTTONDOWN:
        clean=True
    elif event==cv2.EVENT_MOUSEMOVE:
        if clean==True:
            cv2.rectangle(feild,(x,y),(x+s,y+s),(255,255,255),-1)
    elif event==cv2.EVENT_RBUTTONUP:
        clean=False



feild=np.zeros([500,500,3],np.uint8)
feild[:]=255
cv2.namedWindow("paint")
cv2.setMouseCallback("paint",brush)

cv2.namedWindow("setting")
cv2.createTrackbar("red","setting",0,255,nothing)
cv2.createTrackbar("green","setting",0,255,nothing)
cv2.createTrackbar("blue","setting",0,255,nothing)
cv2.createTrackbar("size","setting",5,10,nothing)

while (1):
    k=cv2.waitKey(1)
    if k==27:
        break
    if k==ord('r'):
        feild[:]=255
    if k==ord('s'):
        cv2.imwrite("paint.png",feild)
    r=cv2.getTrackbarPos("red","setting")
    g=cv2.getTrackbarPos("green","setting")
    b=cv2.getTrackbarPos("blue","setting")
    s=cv2.getTrackbarPos("size","setting")  

    cv2.imshow("paint",feild)      

cv2.destroyAllWindows()