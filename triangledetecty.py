import numpy as np
import cv2  
from matplotlib import pyplot as plt 
i=0
img=cv2.imread('1.png',1)
list_redhouses_in_burn_region=[]
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red=np.array([0,100,100])
upper_red=np.array([10,255,255])
mask = cv2.inRange(img_hsv, lower_red, upper_red)
#cv2.imshow('mask',mask)
lower_brown=np.array([4,15,31])
upper_brown=np.array([30,255,255])
mask3=cv2.inRange(img_hsv, lower_brown, upper_brown)
mask45=mask3+mask
contours, hierarchy = cv2.findContours(mask45, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
 approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
 if len(approx)==3:

    
     
     i=i+1

#cv2.imshow('maskbrowngrass',mask3)

#x=cv2.bitwise_or(mask,mask3)
#cv2.imshow("hellnaww",x)
cv2.imshow("m",mask45)
#cv2.imshow("mask",mask)
#if img[mask3>0] :
#cv2.imshow("re",mask45) 
print(i)


cv2.waitKey(0)