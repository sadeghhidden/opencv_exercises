from array import array
import cv2
import numpy as np

x1:int=0
x2:int=0
y1:int=0
y2:int=0
drawing=False
crop=False

def draw(event,x,y,flags,param):
    global crop,drawing,arr,x1,x2,y1,y2
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        crop=True
       
        x1,y1=x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if crop==True:
                
                cv2.rectangle(img,(x1,y1),(x,y),(0,0,255),-1)        
    elif event==cv2.EVENT_LBUTTONUP:
        if crop==True:
            drawing=False
            x2,y2=x,y
            img[:]=(20,20,20)
            img[y1:y2,x1:x2]=(255,255,255)                
    
img=np.zeros((500,500,3),np.uint8)
img[:]=255
cv2.namedWindow('sadegh')
cv2.setMouseCallback('sadegh',draw)
while True:
    k=cv2.waitKey(1)
    if k==27:
        break
    cv2.imshow('sadegh',img)
cv2.destroyAllWindows()    