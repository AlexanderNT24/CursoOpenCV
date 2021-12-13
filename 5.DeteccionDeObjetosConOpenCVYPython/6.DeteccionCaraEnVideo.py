import matplotlib.pyplot as plt
import numpy as np
import cv2

#Usamos hardcascade para analizar la imagen
#Cargamos el fichero con todos los emparejamientos del rostro
#https://stackoverflow.com/questions/30508922/error-215-empty-in-function-detectmultiscale
cascadaCara=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

#Creamos un metodo donde vamos a pasarle como parametro una imagen
def dectectarCara(imagen):
    #Copiamos la imagen con el metodo copy()
    imagen1=imagen.copy()
    #Hardcascade lo que hace es crear muchos rectangulos alrededor de la imagen para cada rostro detectado
    rectangulos=cascadaCara.detectMultiScale(imagen1)
    #Para todos los rostros detectados
    for (x,y,w,h) in rectangulos:
        #Dibujamos un rectangulo
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)
    return imagen1
#Cargamos el fichero con los emparejamientos de los ojos
#https://stackoverflow.com/questions/30508922/error-215-empty-in-function-detectmultiscale
cascadaOjos = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
def dectectarOjos(imagen):
    imagen1=imagen.copy()
    rectangulos=cascadaOjos.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)
    return imagen1    

captura=cv2.VideoCapture(0)

while True:
    resultado,video=captura.read()
    video=dectectarCara(video)
    video=dectectarOjos(video)
    cv2.imshow("Detectar Rostros",video)
    tecla=cv2.waitKey(1)
    if tecla==27:
        break

captura.relase()
cv2.destroyAllWindows()