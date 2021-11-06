import matplotlib.pyplot as plt
import numpy as np
import cv2

imagen=np.zeros(shape=(500,500,3),dtype=np.int16)

fuente=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(imagen,text='Nya',org=(20,100),fontFace=fuente,fontScale=3,color=(0,255,0),thickness=4,lineType=cv2.LINE_8)


plt.imshow(imagen)
plt.show()