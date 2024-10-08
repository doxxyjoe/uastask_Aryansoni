import numpy as np
import cv2  
from matplotlib import pyplot as plt
img=cv2.imread('1.png',1)
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()
cv2.waitKey(0)