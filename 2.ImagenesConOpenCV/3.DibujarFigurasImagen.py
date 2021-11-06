import matplotlib.pyplot as plt
import numpy as np
import cv2

imagen=np.zeros(shape=(500,500,3),dtype=np.int16)

print(imagen.shape)

#pt1=esquinaSup,pt2=EsquinaInf
cv2.rectangle(imagen,pt1=(20,20),pt2=(100,100),color=(255,0,0),thickness=10)
cv2.circle(imagen,center=(250,250),radius=100,color=(0,255,0),thickness=10)
cv2.line(imagen,pt1=(0,400),pt2=(500,400),color=(0,0,255),thickness=10)

plt.imshow(imagen)
plt.show()