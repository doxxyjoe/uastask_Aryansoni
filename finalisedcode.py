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

def uastask(imgsrc):
    
    img=cv2.imread(imgsrc,1)
    img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #masking red color houses
    lower_red=np.array([0,100,100])
    upper_red=np.array([10,255,255])
    mask = cv2.inRange(img_hsv, lower_red, upper_red)
    #cv2.imshow('mask',mask)
    #masking blue houses
    lower_blue=np.array([110,100,100])
    higher_blue=np.array([130,255,255])
    maskblue=cv2.inRange(img_hsv, lower_blue, higher_blue)
    
    #masking green grass aka unburnt region
    lower_green=np.array([40,40,50])
    higher_green=np.array([75,255,255])
    mask2 = cv2.inRange(img_hsv, lower_green, higher_green)
    #cv2.imshow("coloured",img)
#masking brown area
    lower_brown=np.array([4,15,31])
    upper_brown=np.array([30,255,255])
    mask3=cv2.inRange(img_hsv, lower_brown, upper_brown)
    #cv2.imshow('maskbrowngrass',mask3)
    img[mask2>0]=(170,205,102)#GREEN REGION TO CYAN
    img[mask3>0]=(0,255,255)#BROWN REGION TO YELLOW
    x=cv2.bitwise_or(mask3,mask)
    t1=contourfig(x) # red houses in green region
    y=cv2.bitwise_or(mask3,maskblue)
    t2=contourfig(y)# blue houses in green region 
    z=cv2.bitwise_or(mask2,maskblue)
    t3=contourfig(z) #blue houses in brown region
    w=cv2.bitwise_or(mask2,mask)
    t4=contourfig(w)#red houses in brown region 
    a=[t3+t4,t1+t2]
    return a 
def priority(imgsrc):
    
    img=cv2.imread(imgsrc,1)
    img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #masking red color houses
    lower_red=np.array([0,100,100])
    upper_red=np.array([10,255,255])
    mask = cv2.inRange(img_hsv, lower_red, upper_red)
    #cv2.imshow('mask',mask)
    #masking blue houses
    lower_blue=np.array([110,100,100])
    higher_blue=np.array([130,255,255])
    maskblue=cv2.inRange(img_hsv, lower_blue, higher_blue)
    
    #masking green grass aka unburnt region
    lower_green=np.array([40,40,50])
    higher_green=np.array([75,255,255])
    mask2 = cv2.inRange(img_hsv, lower_green, higher_green)
    #cv2.imshow("coloured",img)
#masking brown area
    lower_brown=np.array([4,15,31])
    upper_brown=np.array([30,255,255])
    mask3=cv2.inRange(img_hsv, lower_brown, upper_brown)
    #cv2.imshow('maskbrowngrass',mask3)
    img[mask2>0]=(170,205,102)#GREEN REGION TO CYAN
    img[mask3>0]=(0,255,255)#BROWN REGION TO YELLOW
    x=cv2.bitwise_or(mask3,mask)
    t1=contourfig(x) # red houses in green region
    y=cv2.bitwise_or(mask3,maskblue)
    t2=contourfig(y)# blue houses in green region 
    z=cv2.bitwise_or(mask2,maskblue)
    t3=contourfig(z) #blue houses in brown region
    w=cv2.bitwise_or(mask2,mask)
    t4=contourfig(w)#red houses in brown region
    m=[2*t3+t4,2*t2+t1]
    return m
Hb_Hg=[]
IMGSRC=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','10.png','11.png']
for i in IMGSRC:
 Hb_Hg.append(uastask(i))
print("number of houses in brown region to  green region ",Hb_Hg)   

Pb_Pg=[]   
for z in IMGSRC :
   Pb_Pg.append(priority(z))
print("the priority of houses in  brown region and green region ",Pb_Pg)   
image_priority=[]
for a in Pb_Pg:
   
      Pr= a[0]/a[1]
      y=round(Pr,2)
      image_priority.append(y)
print(image_priority)   
dec_priority= dict(zip(IMGSRC, image_priority ))

dec_img_prio= sorted(dec_priority)   
print("images in descending order of priority",dec_img_prio)


                
   


#plt.imshow(img)
#plt.show()

cv2.waitKey(0)