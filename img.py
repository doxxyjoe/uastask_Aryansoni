import numpy as np
import cv2  
from matplotlib import pyplot as plt 
def contourfig(source):
    i=0
    contours, hierarchy = cv2.findContours(source, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
     approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
     if len(approx)==3:
       i=i+1
    return i

img=cv2.imread('3.png',1)
#masking red color 
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red=np.array([0,100,100])
upper_red=np.array([10,255,255])
mask = cv2.inRange(img_hsv, lower_red, upper_red)
cv2.imshow('redmask',mask)
#masking green grass aka unburnt region
lower_blue=np.array([110,100,100])
higher_blue=np.array([130,255,255])
maskblue=cv2.inRange(img_hsv, lower_blue, higher_blue)
cv2.imshow("bluemask",maskblue)
lower_green=np.array([40,40,50])
higher_green=np.array([75,255,255])
mask2 = cv2.inRange(img_hsv, lower_green, higher_green)
cv2.imshow('maskgreengrass',mask2)

#masking brown area
lower_brown=np.array([4,15,31])
upper_brown=np.array([30,255,255])
mask3=cv2.inRange(img_hsv, lower_brown, upper_brown)
a=cv2.imshow('maskbrowngrass',mask3)
img[mask3>0]=(0,255,255)
img[mask2>0]=(170,205,102)

cv2.imshow("coloured",img)
x=cv2.bitwise_or(mask,mask3)#performing red and brown mask
cv2.imshow("f",x)
print(contourfig(x))

#plt.imshow(img)
#plt.show()
cv2.waitKey(0)


